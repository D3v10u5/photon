Summary:        Libxslt-1.1.29
Name:           libxslt
Version:        1.1.29
Release:        2%{?dist}
License:        MIT
URL:            http:/http://xmlsoft.org/libxslt/
Group:          System Environment/General Libraries
Vendor:         VMware, Inc.
Distribution:   Photon
Source0:        http://xmlsoft.org/sources/%{name}-%{version}.tar.gz
%define sha1    libxslt=edcaeabb3555ae44853bdc406ee9521fb65c620d
Requires:       libxml2-devel
BuildRequires:  libxml2-devel
BuildRequires:  python2
%description
The libxslt package contains XSLT libraries used for extending libxml2 libraries to support XSLT files. 

%package devel
Summary: Development Libraries for libxslt
Group: Development/Libraries
Requires: libxslt = %{version}-%{release}
%description devel
Header files for doing development with libxslt.

%prep
%setup -q
%build
./configure \
    --prefix=%{_prefix} \
    --bindir=%{_bindir} \
    --libdir=%{_libdir} \
    --disable-static \
    --without-python
make %{?_smp_mflags}
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
find %{buildroot} -name '*.la' -delete
%{_fixperms} %{buildroot}/*

%check
make %{?_smp_mflags} check

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%clean
rm -rf %{buildroot}/*
%files
%defattr(-,root,root)
%{_libdir}/*.so.*
%{_libdir}/*.sh
%{_libdir}/libxslt-plugins
%{_bindir}/*
%{_mandir}/man1/*

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_includedir}/*
%{_docdir}/*
%{_datadir}/aclocal/*
%{_mandir}/man3/*

%changelog
*   Wed Dec 07 2016 Xiaolin Li <xiaolinl@vmware.com> 1.1.29-2
-   Moved man3 to devel subpackage.
*   Fri Oct 21 2016 Vinay Kulkarni <kulkarniv@vmware.com> 1.1.29-1
-   Fix CVEs 2016-1683, 2016-1684, 2015-7995 with version 1.1.29
*   Mon Oct 03 2016 Chang Lee <changlee@vmware.com> 1.1.28-4
-   Modified check
*   Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.1.28-3
-   GA - Bump release of all rpms
*   Tue Jan 19 2016 Xiaolin Li <xiaolinl@vmware.com> 1.1.28-2
-   Add a dev subpackage.
*   Mon Oct 13 2014 Divya Thaluru <dthaluru@vmware.com> 1.1.28-1
-   Initial build.  First version
