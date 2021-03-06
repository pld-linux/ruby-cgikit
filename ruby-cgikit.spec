%define pkgname cgikit
Summary:	Ruby CGIKit Library
Summary(pl.UTF-8):	Biblioteka Ruby CGIKit
Name:		ruby-%{pkgname}
Version:	1.0b5
Release:	2.1
License:	GPL
Group:		Development/Libraries
Source0:	http://www.freepan.org/canon/s/su/SuzukiTetsuya/ruby/cgikit/%{pkgname}-%{version}.tar.gz
# Source0-md5:	268c4b807d983486ba54dded24b2c173
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
Obsoletes:	cgikit < 1.0b5-2.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby CGIKit Library.

%description -l pl.UTF-8
Biblioteka Ruby CGIKit.

%prep
%setup -q -n  %{pkgname}-%{version}
mv %{pkgname}-%{version}/* .

%build
ruby install.rb config \
	--prefix=%{_prefix} \
	--site-ruby=%{ruby_rubylibdir} \
	--so-dir=%{ruby_archdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_rubylibdir}
ruby install.rb install --prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{ruby_rubylibdir}/cgikit.rb
%dir %{ruby_rubylibdir}/cgikit
%dir %{ruby_rubylibdir}/cgikit/components
%{ruby_rubylibdir}/cgikit/components/CKErrorPage
%dir %{ruby_rubylibdir}/cgikit/elements
