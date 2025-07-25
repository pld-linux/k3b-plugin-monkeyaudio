Summary:	Monkey Audio plugin for k3b
Summary(pl.UTF-8):	Wtyczka Monkey Audio dla k3b
Name:		k3b-plugin-monkeyaudio
Version:	3.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/k3b/k3bmonkeyaudioplugin-%{version}.tar.bz2
# Source0-md5:	7ca0a8f9fcf9c2695e8e3484c7ce58a9
URL:		http://www.k3b.org/
Patch0:		kde-am.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	k3b-devel
BuildRequires:	libsamplerate-devel
%ifarch %{ix86}
BuildRequires:	nasm
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
K3B plugin to support encoding and decoding of Monkey Audio files.

The Monkey Audio SDK itself is released under a BSD-like license; see
%{_docdir}/%{_name}/LICENSE.libmonkeyaudio* .

%description -l pl.UTF-8
Wtyczka K3B do obsługi kodowania i dekodowania plików Monkey Audio.

Samo Monkey Audio SDK zostało wydane na licencji w stylu BSD -
szczegóły w pliku %{_docdir}/%{_name}/LICENSE.libmonkeyaudio* .

%prep
%setup -q -n k3bmonkeyaudioplugin-%{version}
%patch -P0 -p1

%build
%{__make} -f admin/Makefile.common cvs

%configure \
	--%{!?debug:dis}%{?debug:en}able-debug \
	%{!?debug:--disable-rpath} \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang k3bmonkeyplugin --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f k3bmonkeyplugin.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_libdir}/kde3/lib*.la
%attr(755,root,root) %{_libdir}/kde3/lib*.so*
%{_datadir}/apps/k3b/plugins/*.plugin
