Summary:	Default GTK+2 theme engines
Summary(pl):	Motywy do GTK+2
Name:		gtk2-engines
Version:	2.2.0
Release:	1
Epoch:		1
License:	GPL
Group:		Themes/Gtk
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtk-engines/2.2/gtk-engines-%{version}.tar.bz2
URL:		http://gtk.themes.org/
Requires:	gtk+2 >= 2.2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	gtk+2-devel >= 2.2
Obsoletes:	gtk-engines = 1.9.0
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

%{__make} install DESTDIR=$RPM_BUILD_ROOT

# .la are not needed (according to spec included to package)
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.2.*/engines/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%dir %{_libdir}/gtk-2.0/2.2.*/engines
%attr(755,root,root) %{_libdir}/gtk-2.0/2.2.*/engines/*.so
%{_pkgconfigdir}/*
%{_datadir}/themes/Metal
%{_datadir}/themes/Redmond95
