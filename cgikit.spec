%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define ruby_archdir %(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
Summary:	Ruby CGIKit Library
Name:		cgikit
Version:	1.0b5
Release:	1
License:	GPL
Source0:	http://www.freepan.org/canon/s/su/SuzukiTetsuya/ruby/cgikit/%{name}-%{version}.tar.gz
# Source0-md5:	268c4b807d983486ba54dded24b2c173
Group:		Development/Libraries
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch
BuildRequires:	ruby

%description
Ruby CGIKit Library

%prep
%setup -q -n %{name}-%{version}/%{name}-%{version}

%build
ruby install.rb config \
	--prefix=%{_prefix} \
	--site-ruby=%{ruby_rubylibdir} \
	--so-dir=%{ruby_archdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{ruby_rubylibdir}
ruby install.rb install --prefix=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{ruby_rubylibdir}/cgikit.rb
%dir %{ruby_rubylibdir}/cgikit
%dir %{ruby_rubylibdir}/cgikit/components
%{ruby_rubylibdir}/cgikit/components/CKErrorPage
%dir %{ruby_rubylibdir}/cgikit/elements

%clean
rm -rf $RPM_BUILD_ROOT