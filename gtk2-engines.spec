Summary:	Default GTK+2 theme engines
Summary(pl.UTF-8):	Motywy do GTK+2
Name:		gtk2-engines
Version:	2.14.3
Release:	1
Epoch:		1
License:	GPL v2+ and LGPL v2+
Group:		Themes/GTK+
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtk-engines/2.14/gtk-engines-%{version}.tar.bz2
# Source0-md5:	be92ddda833defb7296a850331c03d05
URL:		http://gtk.themes.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.12.8
BuildRequires:	intltool >= 0.37.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires(post):	gtk+2 >= 2:2.12.9-3
Requires:	gtk+2 >= 2:2.12.8
Provides:	gnome-themes-Clearlooks
Provides:	gnome-themes-ThinIce
Provides:	gtk2-theme-engine-Clearlooks
Provides:	gtk2-theme-engine-Industrial
Provides:	gtk2-theme-engine-Smooth
Provides:	gtk2-theme-engine-ThinIce
Obsoletes:	gnome-themes-LighthouseBlue
Obsoletes:	gnome-themes-LighthouseBlue
Obsoletes:	gnome-themes-ThinIce
Obsoletes:	gtk-engines = 1.9.0
Obsoletes:	gtk2-theme-engine-Industrial
Obsoletes:	gtk2-theme-engine-Smooth
Obsoletes:	gtk2-theme-engine-ThinIce
Obsoletes:	gtk2-theme-engine-lighthouseblue
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%if "%{_lib}" != "lib"
%define		libext		%(lib="%{_lib}"; echo ${lib#lib})
%define		_gtkconfdir	/etc/gtk%{libext}-2.0
%define		pqext		-%{libext}
%else
%define		_gtkconfdir	/etc/gtk-2.0
%define		pqext		%{nil}
%endif

%description
These are the graphical engines for the various GTK+ toolkit themes.

%description -l pl.UTF-8
Pakiet ten zawiera moduły różnych motywów do biblioteki GTK+.

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
gdk-pixbuf-query-loaders%{pqext} > %{_gtkconfdir}/gdk-pixbuf.loaders
exit 0

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%dir %{_datadir}/gtk-engines
%{_datadir}/gtk-engines/*.xml
%dir %{_datadir}/themes/Redmond
%{_datadir}/themes/Clearlooks
%{_datadir}/themes/Crux
%{_datadir}/themes/Industrial
%{_datadir}/themes/Mist
%{_datadir}/themes/Redmond/gtk-2.0
%{_datadir}/themes/ThinIce
%attr(755,root,root) %{_libdir}/gtk-2.0/*/engines/*.so
%{_pkgconfigdir}/gtk-engines-2.pc
