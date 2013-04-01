VERSION=0.7
PREFIX=devel

build-all:
	echo nothing to be done.

dist:
	rm -f pacifica-${PREFIX}-brand-${VERSION}.tar.gz
	rm -f pacifica-${PREFIX}-brand-${VERSION}
	ln -s src pacifica-${PREFIX}-brand-${VERSION}
	tar --exclude '.svn' --exclude 'packages' -zcvf pacifica-${PREFIX}-brand-${VERSION}.tar.gz pacifica-${PREFIX}-brand-${VERSION}/*

rpm: dist
	rm -rf `pwd`/packages
	mkdir -p `pwd`/packages/src
	mkdir -p `pwd`/packages/bin
	rpmbuild -ta pacifica-${PREFIX}-brand-${VERSION}.tar.gz --define '_rpmdir '`pwd`'/packages/bin' --define '_srcrpmdir '`pwd`'/packages/src'

rpms: rpm

MOCKOPTS=
MOCKDIST=fedora-18-x86_64
MOCK=/usr/bin/mock

mock: dist
	rm -rf packages/"$(MOCKDIST)"
	mkdir -p packages/"$(MOCKDIST)"/srpms
	mkdir -p packages/"$(MOCKDIST)"/bin
	$(MOCK) -r "$(MOCKDIST)" --buildsrpm --spec src/pacifica-$(PREFIX)-brand.spec $(MOCKOPTS) --sources "`pwd`"
	mv "/var/lib/mock/$(MOCKDIST)/result/"*.src.rpm packages/"$(MOCKDIST)"/srpms/
	$(MOCK) -r "$(MOCKDIST)" --result "$(CURDIR)"/packages/"$(MOCKDIST)"/bin $(MOCKOPTS) "$(CURDIR)"/packages/"$(MOCKDIST)"/srpms/*.src.rpm
