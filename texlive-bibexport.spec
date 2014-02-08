# revision 26313
# category Package
# catalog-ctan /biblio/bibtex/utils/bibexport
# catalog-date 2011-12-03 09:04:10 +0100
# catalog-license lppl1.3
# catalog-version 3.01
Name:		texlive-bibexport
Version:	3.01
Release:	4
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


%changelog
* Tue Aug 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.01-3
+ Revision: 811972
- Update to latest release.

* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.01-2
+ Revision: 749603
- Rebuild to reduce used resources

* Fri Dec 09 2011 Paulo Andrade <pcpa@mandriva.com.br> 3.01-1
+ Revision: 739690
- texlive-bibexport

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.20-1
+ Revision: 717917
- texlive-bibexport
- texlive-bibexport
- texlive-bibexport
- texlive-bibexport
- texlive-bibexport

