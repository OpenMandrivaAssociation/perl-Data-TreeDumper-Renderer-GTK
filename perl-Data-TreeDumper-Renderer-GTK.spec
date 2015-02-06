%define upstream_name    Data-TreeDumper-Renderer-GTK
%define upstream_version 0.02

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Gtk2::TreeView\\)'
%else
%define _requires_exceptions perl(Gtk2::TreeView)
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Gtk2::TreeView renderer for Data::TreeDumper
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Data::TreeDumper)
BuildRequires:	perl(Term::Size)
BuildRequires:	perl(Gtk2)
BuildRequires:	x11-server-xvfb
Requires:	perl(Term::Size)
BuildArch:	noarch

%description
GTK-perl renderer for *Data::TreeDumper*. 

This widget is the gui equivalent of Data::TreeDumper; it will display a
perl data structure in a TreeView, allowing you to fold and unfold child
data structures and get a quick feel for what's where. Right-clicking
anywhere in the view brings up a context menu, from which the user can
choose to expand or collapse all items.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
xvfb-run make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Data
%{perl_vendorlib}/auto/Data

%changelog
* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 0.20.0-2mdv2011.0
+ Revision: 681384
- mass rebuild

* Wed Aug 05 2009 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.0
+ Revision: 410151
- rebuild using %%perl_convert_version

* Sun Aug 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-1mdv2009.0
+ Revision: 277945
- update to new version 0.02

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.01-3mdv2009.0
+ Revision: 268412
- rebuild early 2009.0 package (before pixel changes)

* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-2mdv2009.0
+ Revision: 213803
- fix dependencies

* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-1mdv2009.0
+ Revision: 213705
- import perl-Data-TreeDumper-Renderer-GTK


* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-1mdv2009.0
- first mdv release
