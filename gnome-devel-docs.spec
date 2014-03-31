Summary:	GNOME Developer Documentation
Summary(pl.UTF-8):	Dokumentacja programisty GNOME
Name:		gnome-devel-docs
Version:	3.12.0
Release:	1
License:	GFDL
Group:		Documentation
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-devel-docs/3.12/%{name}-%{version}.tar.xz
# Source0-md5:	039ea2669864971821a3be843b794edc
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-dtd44-xml
BuildRequires:	gettext-devel
BuildRequires:	itstool
BuildRequires:	libxml2-progs
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.198
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the GNOME Handbook, the GNOME Documentation
Style Guide and an Overview of the GNOME Platform.

%description -l pl.UTF-8
Ten pakiet zawiera podręczniki: "GNOME Handbook", "GNOME Documentation
Style Guide" oraz "Overview of the GNOME Platform".

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
