%define upstream_name	 Data-Validate-IP
%define upstream_version 0.27

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Perl module for validating IP address data

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/Data::Validate::IP
Source0:	https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(NetAddr::IP)
# For tests
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Requires)

%description
Data::Validate::IP - IPv4 and IPv6 validation methods

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%make_install

%files
%{perl_vendorlib}/Data/Validate/IP.pm
%{_mandir}/man3/*.3*
