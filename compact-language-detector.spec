Name:		compact-language-detector
Version:	0.1
Release:	1%{?dist}
Summary:	Language Detection library, as extracted from Google Chromium code

Group:		System Environment/Libraries
License:	BSD
URL:		http://code.google.com/p/chromium-compact-language-detector/
Source0:	http://chromium-compact-language-detector.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	automake, autoconf, libtool

%description
This library will detect the language of any inputed natural language text,
with reliability numbers.

%package	devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header
files for developing applications that use %{name}.


%package	python
Summary:	Python bindings for %{name}
Group:		System Environment/Libraries
Requires:	%{name} = %{version}-%{release}

%description python
Python bindings for %{name}.


%prep
%setup -q


%build
#automake --add-missing
#autoreconf --install
#cd bindings/python
#autoreconf --install

%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

rm -f %{buildroot}/%{_libdir}/*.la

strip %{buildroot}/%{_libdir}/libcld.so.0.0.0


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING README INSTALL
%{_libdir}/*.so.*


%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/cld/*


%changelog
* Mon Jul 30 2012 Arkady L. Shane <ashejn@russianfedora.ru> - 0.1-1.R
- initial build
