Summary:	GNOME Developer Documentation
Summary(pl.UTF-8):	Dokumentacja programisty GNOME
Name:		gnome-devel-docs
Version:	2.21.1
Release:	1
License:	GFDL
Group:		Documentation
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-devel-docs/2.21/%{name}-%{version}.tar.bz2
# Source0-md5:	cc7a62870b52be366875b2a9def12ee8
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-doc-utils >= 0.12.1
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.198
Requires(post,postun):	scrollkeeper
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
	--disable-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --with-omf --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post

%postun
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
