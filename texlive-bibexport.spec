# revision 29349
# category Package
# catalog-ctan /biblio/bibtex/utils/bibexport
# catalog-date 2011-12-03 09:04:10 +0100
# catalog-license lppl1.3
# catalog-version 3.01
Name:		texlive-bibexport
Version:	3.03
Release:	1
Summary:	Extract a BibTeX file based on a .aux file
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/utils/bibexport
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibexport.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibexport.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibexport.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-bibexport.bin = %{EVRD}

%description
A Bourne shell script that uses BibTeX to extract bibliography
entries that are \cite'd in a document. It can also expand a
BibTeX file, expanding the abbreviations (other than the built-
in ones like month names) and following the cross-references.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/bibexport
%{_texmfdistdir}/bibtex/bst/bibexport/expcites.bst
%{_texmfdistdir}/bibtex/bst/bibexport/expkeys.bst
%{_texmfdistdir}/bibtex/bst/bibexport/export.bst
%{_texmfdistdir}/scripts/bibexport/bibexport.sh
%doc %{_texmfdistdir}/doc/bibtex/bibexport/README
%doc %{_texmfdistdir}/doc/bibtex/bibexport/bibexport.pdf
#- source
%doc %{_texmfdistdir}/source/bibtex/bibexport/bibexport.dtx
%doc %{_texmfdistdir}/source/bibtex/bibexport/bibexport.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/bibexport/bibexport.sh bibexport
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
