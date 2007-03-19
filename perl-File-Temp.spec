#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	Temp
Summary:	File::Temp - return name and handle of a temporary file safely
#Summary(pl.UTF-8):	
Name:		perl-File-Temp
Version:	0.18
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/T/TJ/TJENNESS/File-Temp-0.18.tar.gz
# Source0-md5:	9ff2306433a0470773b0b51a70e81a91
URL:		http://search.cpan.org/dist/File-Temp/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::Temp can be used to create and open temporary files in a safe way.
There is both a function interface and an object-oriented interface.
The File::Temp constructor or the tempfile() function can be used
to return the name and the open filehandle of a temporary file.
The tempdir() function can be used to create a temporary directory.

# %description -l pl.UTF-8
# TODO

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
%doc ChangeLog README
%{perl_vendorlib}/File/*.pm
%{_mandir}/man3/*
