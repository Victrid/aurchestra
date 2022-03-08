from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from Database import Base, init_db


class Package(Base):
    """
    Model: The package refers to a whole collection of all versions with the same package name.
    like "acl-1.1.1", "acl-1.1.2" all refers to one Package(name="acl").
    """
    __tablename__: str = 'package'
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(250), nullable=False, unique=True)

    def __str__(self):
        return self.name


class PackageReference(Base):
    """
    Model: The package reference refers to a specific version of a package.
    This is unique.
    """
    __tablename__ = 'package_reference'
    id = Column(Integer, primary_key=True)
    package_id = Column(Integer, ForeignKey('package.id'))
    package = relationship('Package')
    info_file = Column(Text)
    desc_file = Column(Text)
    version = Column(String(100), nullable=False)
    created_at = Column(DateTime)

    def __str__(self):
        return "{}-{}:{}".format(self.package.name, self.version, self.created_at)


class CurrentPackageVersion(Base):
    """
    Model: The current package refers to the current serving version of a package.
    """
    __tablename__ = 'current_package_version'
    id = Column(Integer, primary_key=True)
    package_ref_id: int = Column(Integer, ForeignKey('package_reference.id'))
    package_ref: PackageReference = relationship('PackageReference')
    package_id: int = Column(Integer, ForeignKey('package.id'))
    package: Package = relationship('Package')

    def __str__(self):
        return "{}-{}:{}".format(self.package.name, self.package_ref.version, self.package_ref.created_at)


class PendingPackage(Base):
    """
    Model: The pending package refers to a package that has been uploaded and waiting to be updated.
    """
    __tablename__ = 'pending_package'
    id = Column(Integer, primary_key=True)
    package_ref_id = Column(Integer, ForeignKey('package_reference.id'))
    package_ref = relationship('PackageReference')

    def __str__(self):
        return "{}-{}:{}".format(self.package_ref.package.name, self.package_ref.version, self.package_ref.created_at)


init_db()
