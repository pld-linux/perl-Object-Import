#
# Conditional build:
%bcond_without	tests		# perform "make test"
#
%define	pdir	Object
%define	pnam	Import
Summary:	Object::Import - import methods of an object as functions to a package
Summary(pl.UTF-8):	Object::Import - importuje do pakietu metody obiektowe jako funkcje
Name:		perl-Object-Import
Version:	1.004
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b2beba35458bd6eae6e4079ef662c8eb
URL:		http://search.cpan.org/dist/Object-Import/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module lets you call methods of a certain object more easily by
exporting them as functions to a package. The exported functions are
not called as methods and do not receive an object argument, but
instead the object is fixed at the time you import them with this
module.

%description -l pl.UTF-8
Ten moduł pozwala w łatwiejszy sposób wywoływać metody
obiektowe przez wyeksportowanie ich do pakietu jako funkcji.
Eksportowane funkcje nie są wywoływane jako metody i nie jest im
przekazywana na liście argumentów referencja do obiektu. Zamiast
tego, obiekt, w kontekście którego się wykonują, jest ustalany
w czasie importowanie modułu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorlib}/Object/Import.pm
%{_mandir}/man?/*
