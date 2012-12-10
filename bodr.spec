Name:           bodr
Version:        9
Release:        %mkrel 1
Summary:        The Blue Obelisk Data Repository

Group:          System/Libraries
License:        MIT
URL:            http://blueobelisk.sourceforge.net/wiki/index.php/DataRepository
Source0:        %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-proc
BuildRequires:  pkgconfig

%description
It represents a set of common, standardized data for chemoinformatics
in both XML and plain-text formats. This data is open for common use,
under the expectation that others will contribute to the repository,
either via tabulations of additional properties or revisions/comments
on existing data.

The concept is that via shared default data, reproducing computational
chemistry and chemoinformatics will become more reproducible :-).

Currently this encompasses:
* Elements directory
  * element names and symbols
  * atomic masses, covalent radii, van der Waals radii
  * Pauling electronegativities
  * electron affinity
  * ionization potential
  * default element colors for viewers
* Isotopes directory
  * exact masses of most abundant isotopes
  * isotopic masses and abundances
  * spin
  * kinds of decay, percentages and energy
  * magnetic dipole moment
  * halflife


%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README THANKS TODO
%{_datadir}/%{name}/*.xml
%{_datadir}/%{name}/dicts/*.xml
%{_datadir}/pkgconfig/%{name}.pc






%changelog
* Fri Aug 13 2010 Emmanuel Andry <eandry@mandriva.org> 9-1mdv2011.0
+ Revision: 569387
- New version 9
- use configure2_5x

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 8-2mdv2010.0
+ Revision: 436865
- rebuild

* Tue Feb 24 2009 Emmanuel Andry <eandry@mandriva.org> 8-1mdv2009.1
+ Revision: 344558
- fix URL

* Sun Jun 29 2008 Emmanuel Andry <eandry@mandriva.org> 8-1mdv2009.0
+ Revision: 230033
- New version

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 6-2mdv2008.1
+ Revision: 170778
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Jun 17 2007 Emmanuel Andry <eandry@mandriva.org> 6-1mdv2008.0
+ Revision: 40533
- New version 6


* Mon Mar 05 2007 Nicolas Lécureuil <neoclust@mandriva.org> 5-2mdv2007.0
+ Revision: 132765
- Fix group

* Sun Feb 25 2007 Emmanuel Andry <eandry@mandriva.org> 5-1mdv2007.1
+ Revision: 125499
- Import bodr

