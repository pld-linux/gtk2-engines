Summary:	Default GTK+2 theme engines
Summary(pl.UTF-8):   Motywy do GTK+2
Name:		gtk2-engines
Version:	2.7.4
Release:	1
Epoch:		1
License:	GPL
Group:		Themes/GTK+
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtk-engines/2.7/gtk-engines-%{version}.tar.bz2
# Source0-md5:	b0f27c0f6d5f610ca445a3d82d5779da
URL:		http://gtk.themes.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	gtk+2 >= 2:2.8.0
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

%description -l pl.UTF-8
Pakiet ten zawiera moduły różnych motywów do biblioteki Gtk+.

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
%dir %{_datadir}/themes/Redmond
%{_datadir}/themes/Clearlooks
%{_datadir}/themes/Crux
%{_datadir}/themes/Industrial
%{_datadir}/themes/LighthouseBlue
%{_datadir}/themes/Metal
%{_datadir}/themes/Mist
%{_datadir}/themes/Redmond/gtk-2.0
%{_datadir}/themes/ThinIce
%attr(755,root,root) %{_libdir}/gtk-2.0/*/engines/*.so
%{_pkgconfigdir}/*
