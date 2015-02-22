Summary:	The Blue Obelisk Data Repository
Name:		bodr
Version:	10
Release:	%mkrel 2
License:	MIT
Group:		System/Libraries
Url:		http://blueobelisk.sourceforge.net/
Source0:	http://downloads.sourceforge.net/bodr/%{name}-%{version}.tar.bz2
Source100:	%{name}.rpmlintrc
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	libxslt-proc
BuildArch:	noarch

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
chmod -x README

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog COPYING NEWS README THANKS TODO
%{_datadir}/%{name}/*.xml
%{_datadir}/%{name}/dicts/*.xml
%{_datadir}/pkgconfig/%{name}.pc

