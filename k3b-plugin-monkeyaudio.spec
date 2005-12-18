Summary:	Monkey Audio plugin for k3b
Summary(pl):	Wtyczka Monkey Audio dla k3b
Name:		k3b-plugin-monkeyaudio
Version:	2.0
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/k3b/k3bmonkeyaudioplugin-%{version}.tar.bz2
# Source0-md5:	f35b2c7db9b31bc0b657316055dc8c6c
URL:		http://www.k3b.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	k3b-devel
BuildRequires:	libsamplerate-devel
Requires:	k3b
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
K3B plugin to support encoding and decoding of Monkey Audio files.

The Monkey Audio SDK itself is released under a BSD-like license; see
%{_docdir}/%{_name}/LICENSE.libmonkeyaudio* .

%description -l pl
Wtyczka K3B do obs³ugi kodowania i dekodowania plików Monkey Audio.

Samo Monkey Audio SDK zosta³o wydane na licencji w stylu BSD -
szczegó³y w pliku %{_docdir}/%{_name}/LICENSE.libmonkeyaudio* .

%prep
%setup -q -n k3bmonkeyaudioplugin-%{version}

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common

%configure \
	--%{!?debug:dis}%{?debug:en}able-debug \
	%{!?debug:--disable-rpath} \
	--enable-final \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc src/libmonkeyaudio/LICENSE.libmonkeyaudio
%attr(755,root,root) %{_libdir}/kde3/lib*.so*
%{_libdir}/kde3/lib*.la
%{_datadir}/apps/k3b/plugins/*.plugin
