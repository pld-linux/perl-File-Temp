#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	Temp
#
Summary:	File::Temp - create name and handle of a temporary file safely
Summary(pl.UTF-8):	File::Temp - moduł języka Perl tworzący nazwy plików tymczasowych
Name:		perl-File-Temp
Version:	0.2303
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/File/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7d207d2172b6da5a0c81565324fa565d
URL:		http://search.cpan.org/dist/File-Temp/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.17
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::Temp can be used to create and open temporary files in a safe
way. There is both a function interface and an object-oriented
interface. The File::Temp constructor or the tempfile() function can
be used to return the name and the open filehandle of a temporary
file. The tempdir() function can be used to create a temporary
directory.

%description -l pl.UTF-8
File::Temp może być użyty do tworzenia i otwierania plików
tymczasowych w sposób bezpieczny. Istnieje zarówno interfejs
funkcyjny jak i obiektowy. Konstruktor klasy File::Temp lub funkcja
tempfile() mogą zwracać nazwę pliku tymczasowego a następnie go
otwierać do zapisu. Do tworzenia katalogów tymczasowych może być
użyta funkcja tempdir().

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
%doc README
%{perl_vendorlib}/File/Temp.pm
%{_mandir}/man3/File::Temp.3pm*
