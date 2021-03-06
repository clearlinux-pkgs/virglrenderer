#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : virglrenderer
Version  : 0.9.1
Release  : 1
URL      : https://gitlab.freedesktop.org/virgl/virglrenderer/-/archive/0.9.1/virglrenderer-0.9.1.tar.gz
Source0  : https://gitlab.freedesktop.org/virgl/virglrenderer/-/archive/0.9.1/virglrenderer-0.9.1.tar.gz
Summary  : virgl GL renderer
Group    : Development/Tools
License  : MIT
Requires: virglrenderer-bin = %{version}-%{release}
Requires: virglrenderer-lib = %{version}-%{release}
Requires: virglrenderer-license = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : libepoxy-dev
BuildRequires : pkgconfig(epoxy)
BuildRequires : pkgconfig(libdrm)

%description
The files in this directory help with testing Virgl on the virtio-gpu winsys
by means of Crosvm.

%package bin
Summary: bin components for the virglrenderer package.
Group: Binaries
Requires: virglrenderer-license = %{version}-%{release}

%description bin
bin components for the virglrenderer package.


%package dev
Summary: dev components for the virglrenderer package.
Group: Development
Requires: virglrenderer-lib = %{version}-%{release}
Requires: virglrenderer-bin = %{version}-%{release}
Provides: virglrenderer-devel = %{version}-%{release}
Requires: virglrenderer = %{version}-%{release}

%description dev
dev components for the virglrenderer package.


%package lib
Summary: lib components for the virglrenderer package.
Group: Libraries
Requires: virglrenderer-license = %{version}-%{release}

%description lib
lib components for the virglrenderer package.


%package license
Summary: license components for the virglrenderer package.
Group: Default

%description license
license components for the virglrenderer package.


%prep
%setup -q -n virglrenderer-0.9.1
cd %{_builddir}/virglrenderer-0.9.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1630112016
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/virglrenderer
cp %{_builddir}/virglrenderer-0.9.1/COPYING %{buildroot}/usr/share/package-licenses/virglrenderer/a4924561121fd43cb97468ba0ecce6571b664b29
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/virgl_test_server

%files dev
%defattr(-,root,root,-)
/usr/include/virgl/virglrenderer.h
/usr/lib64/libvirglrenderer.so
/usr/lib64/pkgconfig/virglrenderer.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libvirglrenderer.so.1
/usr/lib64/libvirglrenderer.so.1.5.4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/virglrenderer/a4924561121fd43cb97468ba0ecce6571b664b29
