from datetime import datetime

from falcon import HTTPBadRequest, HTTPNotFound

from ABSPkg import filemgmt
from ABSPkg.PackageStubGenerator import generate_desc, generate_files
from Database import DBSession
from Database.model import CurrentPackageVersion, Package, PackageReference, PendingPackage
from manage.updatehandler import update_database


class PackageHandler:
    def __init__(self):
        self.storage_engine = filemgmt.FileMgmt()

    def on_post(self, req, resp):
        if 'multipart/form-data' not in req.content_type:
            raise HTTPBadRequest('Expected multipart/form-data, not {}'.format(req.content_type))
        form = req.get_media()
        success, filename, pkginfo = self.storage_engine.upload_handler(form)
        if not success:
            raise HTTPBadRequest("Upload failed")
        session = DBSession()
        package = session.query(Package).filter_by(name=pkginfo['name']).first()
        if package is None:
            package = Package(name=pkginfo['name'])
            session.add(package)
        package_ref = PackageReference(package=package, info_file=generate_files(filename),
                                       desc_file=generate_desc(pkginfo), version=pkginfo['version'],
                                       created_at=datetime.now()
                                       )
        session.add(package_ref)
        pending_package = PendingPackage(package_ref=package_ref)
        session.add(pending_package)
        session.commit()
        session.close()
        resp.status_code = 200
        resp.text = 'Package uploaded'
        return

    def on_delete(self, req, resp):
        print("aa")
        if 'application/json' not in req.content_type:
            raise HTTPBadRequest('Expected application/json')
        if 'name' not in req.media:
            raise HTTPBadRequest('Expected name')
        name = req.media['name']
        print(name)
        session = DBSession()
        # get package
        package = session.query(Package).filter_by(name=name).first()
        if package is None:
            raise HTTPNotFound('Package not found')

        # remove CurrentVersion
        session.query(CurrentPackageVersion).filter_by(package=package).delete()
        session.commit()

        # update database
        update_database(session, self.storage_engine)

        # remove orphan package_ref and pending packages
        for item in session.query(PackageReference).filter_by(package=package):
            self.storage_engine.remove_handler(item.desc_file)
            session.query(PendingPackage).filter_by(package_ref=item).delete()
            session.delete(item)
        session.delete(package)
        session.commit()
        session.close()
        resp.status_code = 204
        resp.text = 'Package deleted'
        return
