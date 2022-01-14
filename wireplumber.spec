#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : wireplumber
Version  : 0.4.7
Release  : 423
URL      : file:///aot/build/clearlinux/packages/wireplumber/wireplumber-v0.4.7.tar.gz
Source0  : file:///aot/build/clearlinux/packages/wireplumber/wireplumber-v0.4.7.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: wireplumber-bin = %{version}-%{release}
Requires: wireplumber-data = %{version}-%{release}
Requires: wireplumber-lib = %{version}-%{release}
Requires: wireplumber-services = %{version}-%{release}
BuildRequires : SDL2
BuildRequires : SDL2-dev
BuildRequires : Sphinx
BuildRequires : alsa-lib
BuildRequires : alsa-lib-dev
BuildRequires : alsa-lib-dev32
BuildRequires : alsa-plugins
BuildRequires : alsa-tools
BuildRequires : alsa-tools-dev
BuildRequires : alsa-ucm-conf
BuildRequires : alsa-utils
BuildRequires : autogen
BuildRequires : autogen-dev
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : binutils-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-configure
BuildRequires : buildreq-distutils3
BuildRequires : bzip2-dev
BuildRequires : bzip2-staticdev
BuildRequires : cairo-dev
BuildRequires : clr-avx-tools
BuildRequires : clr-rpm-config
BuildRequires : cmake
BuildRequires : cmake-dev
BuildRequires : docutils
BuildRequires : doxygen
BuildRequires : expat-dev
BuildRequires : expat-staticdev
BuildRequires : fftw-dev
BuildRequires : findutils
BuildRequires : flac-dev
BuildRequires : flac-dev32
BuildRequires : flac-staticdev
BuildRequires : flac-staticdev32
BuildRequires : gcc
BuildRequires : gcc-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libs-math
BuildRequires : gcc-libstdc++32
BuildRequires : gcc-libubsan
BuildRequires : gcc-locale
BuildRequires : glib
BuildRequires : glib-dev
BuildRequires : glibc-dev
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : glibc-staticdev
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : graphviz
BuildRequires : graphviz-extras
BuildRequires : gtk+-dev
BuildRequires : libcanberra-dev
BuildRequires : libcap-dev
BuildRequires : libcap-ng-dev
BuildRequires : libcap-staticdev
BuildRequires : libedit
BuildRequires : libedit-dev
BuildRequires : libfdk_aac-dev
BuildRequires : libfdk_aac-staticdev
BuildRequires : libffi-dev
BuildRequires : libffi-staticdev
BuildRequires : libgcc1
BuildRequires : libogg-dev
BuildRequires : libogg-dev32
BuildRequires : libogg-staticdev
BuildRequires : libogg-staticdev32
BuildRequires : libsndfile-dev
BuildRequires : libsndfile-staticdev
BuildRequires : libstdc++
BuildRequires : libtool-dev
BuildRequires : libusb-dev
BuildRequires : libvorbis-dev
BuildRequires : libvorbis-dev32
BuildRequires : libvorbis-staticdev
BuildRequires : libvorbis-staticdev32
BuildRequires : libxml2-dev
BuildRequires : libxml2-staticdev
BuildRequires : lilv
BuildRequires : lilv-dev
BuildRequires : lilv-staticdev
BuildRequires : lua-dev
BuildRequires : lua-staticdev
BuildRequires : lv2
BuildRequires : lv2-dev
BuildRequires : lxml
BuildRequires : ncurses-dev
BuildRequires : octave-dev
BuildRequires : openssl-dev
BuildRequires : openssl-staticdev
BuildRequires : opus
BuildRequires : opus-dev
BuildRequires : opus-lib
BuildRequires : opus-staticdev
BuildRequires : pcre-dev
BuildRequires : pcre-staticdev
BuildRequires : pcre2-dev
BuildRequires : pcre2-staticdev
BuildRequires : perl
BuildRequires : perl(XML::Parser)
BuildRequires : perl-XML-Parser
BuildRequires : pipewire
BuildRequires : pipewire-dev
BuildRequires : pipewire-tests
BuildRequires : pkg-config
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(avahi-client)
BuildRequires : pkgconfig(bluez)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(gstreamer-1.0)
BuildRequires : pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires : pkgconfig(jack)
BuildRequires : pkgconfig(libcap)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(libusb-1.0)
BuildRequires : pkgconfig(lua)
BuildRequires : pkgconfig(ncurses)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(readline)
BuildRequires : pkgconfig(sbc)
BuildRequires : pkgconfig(sndfile)
BuildRequires : pkgconfig(systemd)
BuildRequires : pkgconfig(x11)
BuildRequires : pulseaudio
BuildRequires : pulseaudio-dev
BuildRequires : pypi(html5lib)
BuildRequires : pypi(importlib_metadata)
BuildRequires : pypi(isodate)
BuildRequires : pypi(pyparsing)
BuildRequires : python-graphviz
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : python3-staticdev
BuildRequires : rdflib
BuildRequires : readline-dev
BuildRequires : rtkit
BuildRequires : rtkit-bin
BuildRequires : rtkit-data
BuildRequires : rtkit-libexec
BuildRequires : rtkit-services
BuildRequires : sed
BuildRequires : serd
BuildRequires : serd-dev
BuildRequires : serd-staticdev
BuildRequires : sord
BuildRequires : sord-dev
BuildRequires : sord-staticdev
BuildRequires : speex-dev
BuildRequires : speex-staticdev
BuildRequires : speexdsp-dev
BuildRequires : speexdsp-staticdev
BuildRequires : sqlite-autoconf-dev
BuildRequires : sratom
BuildRequires : sratom-dev
BuildRequires : sratom-staticdev
BuildRequires : systemd
BuildRequires : systemd-dev
BuildRequires : valgrind
BuildRequires : xz-dev
BuildRequires : xz-staticdev
BuildRequires : yaml-cpp
BuildRequires : yaml-cpp-dev
BuildRequires : zlib-dev
BuildRequires : zlib-staticdev
BuildRequires : zstd-dev
BuildRequires : zstd-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
WirePlumber
===========
.. image:: https://gitlab.freedesktop.org/pipewire/wireplumber/badges/master/pipeline.svg
:alt: Pipeline status

%package bin
Summary: bin components for the wireplumber package.
Group: Binaries
Requires: wireplumber-data = %{version}-%{release}
Requires: wireplumber-services = %{version}-%{release}

%description bin
bin components for the wireplumber package.


%package data
Summary: data components for the wireplumber package.
Group: Data

%description data
data components for the wireplumber package.


%package dev
Summary: dev components for the wireplumber package.
Group: Development
Requires: wireplumber-lib = %{version}-%{release}
Requires: wireplumber-bin = %{version}-%{release}
Requires: wireplumber-data = %{version}-%{release}
Provides: wireplumber-devel = %{version}-%{release}
Requires: wireplumber = %{version}-%{release}

%description dev
dev components for the wireplumber package.


%package lib
Summary: lib components for the wireplumber package.
Group: Libraries
Requires: wireplumber-data = %{version}-%{release}

%description lib
lib components for the wireplumber package.


%package services
Summary: services components for the wireplumber package.
Group: Systemd services

%description services
services components for the wireplumber package.


%package staticdev
Summary: staticdev components for the wireplumber package.
Group: Default
Requires: wireplumber-dev = %{version}-%{release}

%description staticdev
staticdev components for the wireplumber package.


%prep
%setup -q -n wireplumber
cd %{_builddir}/wireplumber

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1642182677
export GCC_IGNORE_WERROR=1
## altflags_pgo content
## pgo generate
unset ASFLAGS
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage -fprofile-partial-training -fprofile-correction -freorder-functions --coverage -lgcov"
export CFLAGS_GENERATE="-ggdb3 -ggnu-pubnames -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=auto -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export ASMFLAGS_GENERATE="-ggdb3 -ggnu-pubnames -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=auto -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export FCFLAGS_GENERATE="-ggdb3 -ggnu-pubnames -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=auto -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export FFLAGS_GENERATE="-ggdb3 -ggnu-pubnames -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=auto -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export CXXFLAGS_GENERATE="-ggdb3 -ggnu-pubnames -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=auto -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export LDFLAGS_GENERATE="-O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=auto -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export LIBS_GENERATE="-lgcov"
## pgo use
## -fno-tree-vectorize: disable -ftree-vectorize thus disable -ftree-loop-vectorize and -ftree-slp-vectorize -fopt-info-vec
## remove: -flimit-function-alignment -fira-loop-pressure
## -O3 -ffast-math
## -funroll-loops maybe dangerous
## -Wl,-z,max-page-size=0x1000
## -pthread -lpthread
## -Wl,-Bsymbolic-functions
export PGO_USE="-Wmissing-profile -Wcoverage-mismatch -fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-partial-training -fprofile-correction -freorder-functions"
export CFLAGS_USE="-ggdb3 -ggnu-pubnames -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=auto -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export ASMFLAGS_USE="-ggdb3 -ggnu-pubnames -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=auto -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export FCFLAGS_USE="-ggdb3 -ggnu-pubnames -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=auto -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export FFLAGS_USE="-ggdb3 -ggnu-pubnames -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=auto -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export CXXFLAGS_USE="-ggdb3 -ggnu-pubnames -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=auto -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export LDFLAGS_USE="-ggdb3 -ggnu-pubnames -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=auto -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#%global _disable_maintainer_mode %{nil}
#
export CCACHE_DISABLE=true
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
#
export PKG_CONFIG_PATH="/usr/lib64/pkgconfig:/usr/share/pkgconfig"
#
export LD_LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export PATH="/usr/lib64/ccache/bin:/usr/local/cuda/bin:/usr/local/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
#
export CPATH="/usr/local/cuda/include"
#
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=1
export __GL_SYNC_DISPLAY_DEVICE=HDMI-0
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=HDMI-0
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH="/usr/share/defaults/fonts"
export GTK_IM_MODULE="xim"
export QT_IM_MODULE="cedilla"
export FREETYPE_PROPERTIES="truetype:interpreter-version=40"
export NO_AT_BRIDGE=1
export GTK_A11Y=none
export PLASMA_USE_QT_SCALING=1
export QT_AUTO_SCREEN_SCALE_FACTOR=0
export QT_ENABLE_HIGHDPI_SCALING=0
export QT_FONT_DPI=88
export GTK_USE_PORTAL=1
export DESKTOP_SESSION=plasma
export GSETTINGS_SCHEMA_DIR="/usr/share/glib-2.0/schemas"
## altflags_pgo end
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
export ASMFLAGS="${ASMFLAGS_GENERATE}"
export LIBS="${LIBS_GENERATE}"

echo PGO Phase 1
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" LIBS="$LIBS" meson --libdir=lib64 --sysconfdir=/usr/share --prefix=/usr --buildtype=plain -Ddefault_library=both  -Ddefault_library=both \
-Dsystem-lua=true \
-Ddoc=disabled \
-Dsystemd=enabled \
-Dsystemd-user-service=true \
-Dintrospection=enabled \
-Delogind=disabled \
-Dtests=true builddir
ninja --verbose %{?_smp_mflags} -C builddir

## profile_payload start
unset LD_LIBRARY_PATH
unset LIBRARY_PATH
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=1
export __GL_SYNC_DISPLAY_DEVICE=HDMI-0
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=HDMI-0
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH=/usr/share/defaults/fonts
export PKG_CONFIG_PATH="/usr/lib64/pkgconfig:/usr/share/pkgconfig"
export LD_LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
meson test --verbose --num-processes 1 -C builddir || :
export LD_LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
## profile_payload end

%install
DESTDIR=%{buildroot} ninja -C builddir install


%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/wireplumber
/usr/bin/wpctl
/usr/bin/wpexec

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Wp-0.4.typelib
/usr/share/gir-1.0/*.gir
/usr/share/wireplumber/bluetooth.conf
/usr/share/wireplumber/bluetooth.lua.d/00-functions.lua
/usr/share/wireplumber/bluetooth.lua.d/30-bluez-monitor.lua
/usr/share/wireplumber/bluetooth.lua.d/50-bluez-config.lua
/usr/share/wireplumber/bluetooth.lua.d/90-enable-all.lua
/usr/share/wireplumber/common/00-functions.lua
/usr/share/wireplumber/main.conf
/usr/share/wireplumber/main.lua.d/00-functions.lua
/usr/share/wireplumber/main.lua.d/20-default-access.lua
/usr/share/wireplumber/main.lua.d/30-alsa-monitor.lua
/usr/share/wireplumber/main.lua.d/30-libcamera-monitor.lua
/usr/share/wireplumber/main.lua.d/30-v4l2-monitor.lua
/usr/share/wireplumber/main.lua.d/40-device-defaults.lua
/usr/share/wireplumber/main.lua.d/50-alsa-config.lua
/usr/share/wireplumber/main.lua.d/50-default-access-config.lua
/usr/share/wireplumber/main.lua.d/50-libcamera-config.lua
/usr/share/wireplumber/main.lua.d/50-v4l2-config.lua
/usr/share/wireplumber/main.lua.d/90-enable-all.lua
/usr/share/wireplumber/policy.conf
/usr/share/wireplumber/policy.lua.d/00-functions.lua
/usr/share/wireplumber/policy.lua.d/10-default-policy.lua
/usr/share/wireplumber/policy.lua.d/50-endpoints-config.lua
/usr/share/wireplumber/policy.lua.d/90-enable-all.lua
/usr/share/wireplumber/scripts/access/access-default.lua
/usr/share/wireplumber/scripts/access/access-portal.lua
/usr/share/wireplumber/scripts/create-item.lua
/usr/share/wireplumber/scripts/default-routes.lua
/usr/share/wireplumber/scripts/intended-roles.lua
/usr/share/wireplumber/scripts/monitors/alsa-midi.lua
/usr/share/wireplumber/scripts/monitors/alsa.lua
/usr/share/wireplumber/scripts/monitors/bluez.lua
/usr/share/wireplumber/scripts/monitors/libcamera.lua
/usr/share/wireplumber/scripts/monitors/v4l2.lua
/usr/share/wireplumber/scripts/policy-endpoint-client-links.lua
/usr/share/wireplumber/scripts/policy-endpoint-client.lua
/usr/share/wireplumber/scripts/policy-endpoint-device.lua
/usr/share/wireplumber/scripts/policy-node.lua
/usr/share/wireplumber/scripts/restore-stream.lua
/usr/share/wireplumber/scripts/static-endpoints.lua
/usr/share/wireplumber/scripts/suspend-node.lua
/usr/share/wireplumber/wireplumber.conf

%files dev
%defattr(-,root,root,-)
/usr/include/wireplumber-0.4/wp/client.h
/usr/include/wireplumber-0.4/wp/component-loader.h
/usr/include/wireplumber-0.4/wp/core.h
/usr/include/wireplumber-0.4/wp/defs.h
/usr/include/wireplumber-0.4/wp/device.h
/usr/include/wireplumber-0.4/wp/endpoint.h
/usr/include/wireplumber-0.4/wp/error.h
/usr/include/wireplumber-0.4/wp/factory.h
/usr/include/wireplumber-0.4/wp/global-proxy.h
/usr/include/wireplumber-0.4/wp/iterator.h
/usr/include/wireplumber-0.4/wp/link.h
/usr/include/wireplumber-0.4/wp/log.h
/usr/include/wireplumber-0.4/wp/metadata.h
/usr/include/wireplumber-0.4/wp/module.h
/usr/include/wireplumber-0.4/wp/node.h
/usr/include/wireplumber-0.4/wp/object-interest.h
/usr/include/wireplumber-0.4/wp/object-manager.h
/usr/include/wireplumber-0.4/wp/object.h
/usr/include/wireplumber-0.4/wp/plugin.h
/usr/include/wireplumber-0.4/wp/port.h
/usr/include/wireplumber-0.4/wp/properties.h
/usr/include/wireplumber-0.4/wp/proxy-interfaces.h
/usr/include/wireplumber-0.4/wp/proxy.h
/usr/include/wireplumber-0.4/wp/session-item.h
/usr/include/wireplumber-0.4/wp/si-factory.h
/usr/include/wireplumber-0.4/wp/si-interfaces.h
/usr/include/wireplumber-0.4/wp/spa-pod.h
/usr/include/wireplumber-0.4/wp/spa-type.h
/usr/include/wireplumber-0.4/wp/state.h
/usr/include/wireplumber-0.4/wp/transition.h
/usr/include/wireplumber-0.4/wp/wp.h
/usr/include/wireplumber-0.4/wp/wpenums.h
/usr/include/wireplumber-0.4/wp/wpversion.h
/usr/lib64/pkgconfig/wireplumber-0.4.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libwireplumber-0.4.so
/usr/lib64/libwireplumber-0.4.so.0
/usr/lib64/libwireplumber-0.4.so.0.4.7
/usr/lib64/wireplumber-0.4/libwireplumber-module-default-nodes-api.so
/usr/lib64/wireplumber-0.4/libwireplumber-module-default-nodes.so
/usr/lib64/wireplumber-0.4/libwireplumber-module-default-profile.so
/usr/lib64/wireplumber-0.4/libwireplumber-module-device-activation.so
/usr/lib64/wireplumber-0.4/libwireplumber-module-file-monitor-api.so
/usr/lib64/wireplumber-0.4/libwireplumber-module-logind.so
/usr/lib64/wireplumber-0.4/libwireplumber-module-lua-scripting.so
/usr/lib64/wireplumber-0.4/libwireplumber-module-metadata.so
/usr/lib64/wireplumber-0.4/libwireplumber-module-mixer-api.so
/usr/lib64/wireplumber-0.4/libwireplumber-module-portal-permissionstore.so
/usr/lib64/wireplumber-0.4/libwireplumber-module-reserve-device.so
/usr/lib64/wireplumber-0.4/libwireplumber-module-route-settings-api.so
/usr/lib64/wireplumber-0.4/libwireplumber-module-si-audio-adapter.so
/usr/lib64/wireplumber-0.4/libwireplumber-module-si-audio-endpoint.so
/usr/lib64/wireplumber-0.4/libwireplumber-module-si-node.so
/usr/lib64/wireplumber-0.4/libwireplumber-module-si-standard-link.so

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/wireplumber.service
/usr/lib/systemd/user/wireplumber@.service

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libwireplumber-0.4.a
