Summary:	Default GTK+ theme engines
Summary(pl):	Tematy do Gtk+
Name:		gtk-engines
Version:	1.9.0
Release:	2
Epoch:		1
License:	GPL
Group:		Themes/Gtk
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/1.9/%{name}-%{version}.tar.bz2
URL:		http://gtk.themes.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	gtk+2-devel
Obsoletes:	gtk-engines = 1.9.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6
%define         _mandir         %{_prefix}/man

%description
These are the graphical engines for the various GTK+ toolkit themes.

%description -l pl
Pakiet ten zawiera modu³y ró¿nych tematów do biblioteki Gtk+.

%prep
%setup -q

%build
libtoolize --copy --force
aclocal
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_libdir}/gtk-2.0/2.0.*/engines

%{_datadir}/themes/Metal
%{_datadir}/themes/Redmond95
