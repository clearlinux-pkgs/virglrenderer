#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v3
# autospec commit: ab27b0e
#
Name     : virglrenderer
Version  : 1.0.1
Release  : 9
URL      : https://gitlab.freedesktop.org/virgl/virglrenderer/-/archive/virglrenderer-1.0.1/virglrenderer-virglrenderer-1.0.1.tar.gz
Source0  : https://gitlab.freedesktop.org/virgl/virglrenderer/-/archive/virglrenderer-1.0.1/virglrenderer-virglrenderer-1.0.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: virglrenderer-bin = %{version}-%{release}
Requires: virglrenderer-lib = %{version}-%{release}
Requires: virglrenderer-license = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : libepoxy-dev
BuildRequires : pkgconfig(epoxy)
BuildRequires : pkgconfig(gbm)
BuildRequires : pkgconfig(libdrm)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
`Virglrenderer <https://virgil3d.github.io/>`_ - The VirGL virtual OpenGL renderer
==================================================================================

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
%setup -q -n virglrenderer-virglrenderer-1.0.1
cd %{_builddir}/virglrenderer-virglrenderer-1.0.1
pushd ..
cp -a virglrenderer-virglrenderer-1.0.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1704925587
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
mkdir -p %{buildroot}/usr/share/package-licenses/virglrenderer
cp %{_builddir}/virglrenderer-virglrenderer-%{version}/COPYING %{buildroot}/usr/share/package-licenses/virglrenderer/a4924561121fd43cb97468ba0ecce6571b664b29 || :
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/virgl_test_server
/usr/bin/virgl_test_server

%files dev
%defattr(-,root,root,-)
/usr/include/virgl/virgl-version.h
/usr/include/virgl/virglrenderer.h
/usr/lib64/libvirglrenderer.so
/usr/lib64/pkgconfig/virglrenderer.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libvirglrenderer.so.1.8.9
/usr/lib64/libvirglrenderer.so.1
/usr/lib64/libvirglrenderer.so.1.8.9

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/virglrenderer/a4924561121fd43cb97468ba0ecce6571b664b29
