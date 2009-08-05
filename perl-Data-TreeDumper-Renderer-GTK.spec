%define upstream_name    Data-TreeDumper-Renderer-GTK
%define upstream_version 0.02

%define _requires_exceptions perl(Gtk2::TreeView)

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Gtk2::TreeView renderer for Data::TreeDumper
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Data::TreeDumper)
BuildRequires: perl(Term::Size)
BuildRequires: perl(Gtk2)
BuildRequires: x11-server-xvfb
Requires: perl(Term::Size)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
xvfb-run make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/Data
%perl_vendorlib/auto/Data
