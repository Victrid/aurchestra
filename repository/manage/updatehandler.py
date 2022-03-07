from sqlalchemy.orm import Session

from ABSPkg import filemgmt
from ABSPkg.filemgmt import FileMgmt
from ABSPkg.packageDB import PackageDB
from Database import DBSession
from Database.model import CurrentPackageVersion, PackageReference, PendingPackage


def update_database(session: Session, storage_engine: FileMgmt):
    # replace CurrentPackageVersion
    for item in session.query(PendingPackage):
        package_stub = item.package_ref.package
        # TODO: removed package_stub: what's the behaviour?
        current = session.query(CurrentPackageVersion).filter_by(package=package_stub).first()
        if current is not None:
            session.delete(current)
        current = CurrentPackageVersion(package=package_stub, package_ref=item.package_ref)
        session.add(current)
        session.delete(item)
    session.commit()

    # Create database file
    database = PackageDB()
    for item in session.query(CurrentPackageVersion):
        database.add_package("{}-{}".format(item.package.name, item.package_ref.version),
                             item.package_ref.info_file,
                             item.package_ref.desc_file
                             )
    database.update_db()

    # Remove old packages
    for current in session.query(CurrentPackageVersion):
        for package_ref in session.query(PackageReference).filter_by(package=current.package):
            if package_ref.id == current.package_ref.id:
                # solve problem in sqlalchemy: id the same
                continue
            else:
                storage_engine.remove_handler(package_ref.desc_file)
                session.delete(package_ref)
    session.commit()


class RepositoryHandler:
    def __init__(self):
        self.storage_engine = filemgmt.FileMgmt()

    def on_put(self, req, resp):
        session = DBSession()
        update_database(session, self.storage_engine)
        session.close()
        resp.status_code = 200
        resp.body = "Repository updated"
        return
