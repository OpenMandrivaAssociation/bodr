Name:           bodr
Version:        6
Release:        %mkrel 2
Summary:        The Blue Obelisk Data Repository

Group:          System/Libraries
License:        MIT
URL:            http://almost.cubic.uni-koeln.de/cdk
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
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README THANKS TODO
%{_datadir}/%{name}/*.xml
%{_datadir}/%{name}/dicts/*.xml
%{_datadir}/pkgconfig/%{name}.pc




