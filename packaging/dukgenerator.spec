Name:           dukgenerator
Version:        1.0.0
Release:        7
License:        Apache-2.0
Summary:        Device Unique Key Library
Group:          Security/Libraries
Source0:        %{name}-%{version}.tar.gz
Source1001: 	dukgenerator.manifest
BuildRequires:  cmake

BuildRequires:  pkgconfig(cryptsvc)
BuildRequires:  pkgconfig(openssl)

%description
Device Unique Key Library.

%package devel
Summary:        Device Unique Key Library
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description devel
Device Unique Key Library (Development Files).

%prep
%setup -q
cp %{SOURCE1001} .

%build
MAJORVER=`echo %{version} | awk 'BEGIN {FS="."}{print $1}'`
%cmake . -DLIB_INSTALL_DIR:PATH=%{_libdir} -DFULLVER=%{version} -DMAJORVER=${MAJORVER} -DDESCRIPTION="%{summary}" -DBUILD_SHARED_LIBS:BOOL=OFF
make %{?_smp_mflags}


%install
make DESTDIR=%{?buildroot:%{buildroot}} INSTALL_ROOT=%{?buildroot:%{buildroot}} install
rm -f %{?buildroot:%{buildroot}}%{_infodir}/dir
find %{?buildroot:%{buildroot}} -regex ".*\\.la$" | xargs rm -f --

%files
%manifest %{name}.manifest
%license LICENSE.APLv2
%{_libdir}/*.a


%files devel
%manifest %{name}.manifest
%{_includedir}/*
%{_libdir}/pkgconfig/dukgenerator.pc
