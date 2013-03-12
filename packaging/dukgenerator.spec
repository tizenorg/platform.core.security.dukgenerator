Name:      dukgenerator 
Summary:   nothing
Version:    1.0.1
Release:    5
Group:      security
License:    Flora
Source0:    %{name}-%{version}.tar.gz

%description
device unique key generator

%prep
%setup -q
%ifarch %{arm}
cp libs/libdukgenerator.arm7l.a libs/libdukgenerator.a
%else
cp libs/libdukgenerator.i586.a libs/libdukgenerator.a
%endif


%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/license
mkdir -p %{buildroot}/usr/lib
mkdir -p %{buildroot}/usr/include
cp LICENSE.Flora %{buildroot}/usr/share/license/%{name}
cp -arf libs/libdukgenerator.a %{buildroot}/usr/lib/libdukgenerator.a
cp -arf inc/dukgen.h %{buildroot}/usr/include/dukgen.h

%files 
%{_libdir}/libdukgenerator.a
%{_includedir}/dukgen.h
%{_datadir}/license/%{name}

