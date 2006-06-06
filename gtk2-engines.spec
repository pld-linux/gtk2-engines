Summary:	Default GTK+2 theme engines
Summary(pl):	Motywy do GTK+2
Name:		gtk2-engines
Version:	2.6.9
Release:	1
Epoch:		1
License:	GPL
Group:		Themes/GTK+
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtk-engines/2.6/gtk-engines-%{version}.tar.bz2
# Source0-md5:	da44fa2cbb89da5abcb40e845e74bc76
URL:		http://gtk.themes.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.8.18
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	gtk+2 >= 2:2.8.18
Provides:	gnome-themes-Clearlooks
Provides:	gnome-themes-LighthouseBlue
Provides:	gnome-themes-ThinIce
Provides:	gtk2-theme-engine-Clearlooks
Provides:	gtk2-theme-engine-Industrial
Provides:	gtk2-theme-engine-Smooth
Provides:	gtk2-theme-engine-ThinIce
Provides:	gtk2-theme-engine-lighthouseblue
Obsoletes:	gnome-themes-LighthouseBlue
Obsoletes:	gnome-themes-ThinIce
Obsoletes:	gtk-engines = 1.9.0
Obsoletes:	gtk2-theme-engine-Industrial
Obsoletes:	gtk2-theme-engine-Smooth
Obsoletes:	gtk2-theme-engine-ThinIce
Obsoletes:	gtk2-theme-engine-lighthouseblue
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These are the graphical engines for the various GTK+ toolkit themes.

%description -l pl
Pakiet ten zawiera modu³y ró¿nych motywów do biblioteki Gtk+.

%prep
%setup -q -n gtk-engines-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# .la are not needed (according to spec included to package)
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/*/engines/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
%{_bindir}/gdk-pixbuf-query-loaders >%{_sysconfdir}/gtk-2.0/gdk-pixbuf.loaders
exit 0

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{_datadir}/themes/Clearlooks
%{_datadir}/themes/Crux
%{_datadir}/themes/Industrial/*
%{_datadir}/themes/LighthouseBlue
%{_datadir}/themes/Metal/*
%{_datadir}/themes/Mist
%{_datadir}/themes/Redmond
%{_datadir}/themes/ThinIce/*
%dir %{_libdir}/gtk-2.0/*/engines
%attr(755,root,root) %{_libdir}/gtk-2.0/*/engines/*.so
%{_pkgconfigdir}/*
