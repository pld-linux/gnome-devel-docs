Summary:	GNOME Developer Documentation
Summary(pl.UTF-8):	Dokumentacja programisty GNOME
Name:		gnome-devel-docs
Version:	2.19.1
Release:	1
License:	GPL
Group:		Documentation
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-devel-docs/2.19/%{name}-%{version}.tar.bz2
# Source0-md5:	6615ea643ec27c41f97858d874bc4eb8
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-doc-utils >= 0.10.3
BuildRequires:	rpmbuild(macros) >= 1.198
Requires(post,postun):	scrollkeeper
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

%find_lang gdp-handbook --with-gnome
%find_lang gdp-style-guide --with-gnome
%find_lang platform-overview --with-gnome
cat gdp-handbook.lang > %{name}.lang
cat gdp-style-guide.lang >> %{name}.lang
cat platform-overview.lang >> %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post

%postun
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_omf_dest_dir}/gdp-handbook
%{_omf_dest_dir}/gdp-handbook/gdp-handbook-C.omf
%dir %{_omf_dest_dir}/gdp-style-guide
%{_omf_dest_dir}/gdp-style-guide/gdp-style-guide-C.omf
%dir %{_omf_dest_dir}/platform-overview
%{_omf_dest_dir}/platform-overview/platform-overview-C.omf
%lang(es) %{_omf_dest_dir}/platform-overview/platform-overview-es.omf
