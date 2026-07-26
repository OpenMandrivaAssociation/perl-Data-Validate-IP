%define upstream_name	 Data-Validate-IP
Name:		perl-%{upstream_name}
Version:	0.27
Release:	3

Summary:	Perl module for validating IP address data

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Data::Validate::IP
Source0:	https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/%{upstream_name}-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(NetAddr::IP)
# For tests
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Requires)

%description
Data::Validate::IP - IPv4 and IPv6 validation methods

%prep
%setup -q -n %{upstream_name}-%{version}

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
