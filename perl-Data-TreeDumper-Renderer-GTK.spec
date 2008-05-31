%define module   Data-TreeDumper-Renderer-GTK
%define version    0.01
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Gtk2::TreeView renderer for Data::TreeDumper
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Data/%{module}-%{version}.tar.gz
BuildRequires: perl(Data::TreeDumper)
BuildRequires: perl(Term::Size)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
GTK-perl renderer for *Data::TreeDumper*. 

This widget is the gui equivalent of Data::TreeDumper; it will display a
perl data structure in a TreeView, allowing you to fold and unfold child
data structures and get a quick feel for what's where. Right-clicking
anywhere in the view brings up a context menu, from which the user can
choose to expand or collapse all items.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

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

