%bcond_with bootstrap
%global packname  DESeq
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.6.1
Release:          2
Summary:          Differential gene expression analysis based on the negative binomial distribution
Group:            Sciences/Mathematics
License:          GPL (>= 3)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-Biobase R-locfit R-genefilter R-geneplotter
Requires:         R-methods R-MASS
%if %{without bootstrap}
Requires:         R-pasilla
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-Biobase
BuildRequires:    R-locfit R-genefilter R-geneplotter R-methods R-MASS
%if %{without bootstrap}
BuildRequires:    R-pasilla
%endif

%description
Estimate variance-mean dependence in count data from high-throughput
sequencing assays and test for differential expression based on a model
using the negative binomial distribution

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extra
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
