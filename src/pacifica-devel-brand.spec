# Just works for rhel5-x86_64 systems.

Name: pacifica-devel-brand
Version: 0.8
Release: 1%{?dist}
Summary: Pacifica Brand
Group: System Environment/Base
License: UNKNOWN
Source: %{name}-%{version}.tar.gz
Requires: myemsl-web %{name}-common
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
Provides: pacifica-brand

%description
Pacifica Devel Brand

%package        ssl
Summary:        Pacifica Devel Brand SSL
Group:          System Environment/Base
Requires: myemsl-web-ssl %{name}-common
BuildArch: noarch
Provides: pacifica-brand-ssl

%description    ssl
Pacifica Devel Brand

%package        common
Summary:        Pacifica Brand Common
Group:          System Environment/Base
Requires: myemsl-web-common
BuildArch: noarch
Provides: pacifica-brand-common

%description    common
Pacifica Brand

%prep
%setup -q

%build
echo "Nothing to Build"

%install
dir=$RPM_BUILD_ROOT/%{_localstatedir}/www/myemsl/brand
mkdir -p $dir
cp -r * $dir/
rm -f $dir/*.spec
rm -f $dir/brand.conf.in
chmod 755 $dir/favicon.ico
dir=$RPM_BUILD_ROOT/%{_prefix}/lib/myemsl/apache/myemsl.d
mkdir -p $dir
sed 's:@WEBAUTH_MYEMSL@:/usr/lib/myemsl/apache/webauth-myemsl.conf:g' brand.conf.in > $dir/brand.conf
dir=$RPM_BUILD_ROOT/%{_prefix}/lib/myemsl/apache/myemsl-ssl.d
mkdir -p $dir
sed 's:@WEBAUTH_MYEMSL@:/usr/lib/myemsl/apache/webauth-myemsl.conf:g' brand.conf.in > $dir/brand.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_prefix}/lib/myemsl/apache/myemsl.d

%files ssl
%defattr(-,root,root)
%{_prefix}/lib/myemsl/apache/myemsl-ssl.d

%files common
%defattr(-,root,root)
%{_localstatedir}/www/myemsl/brand
