%global tl_name bibexport
%global tl_revision 50677

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.03
Release:	%{tl_revision}.1
Summary:	Extract a BibTeX file based on a .aux file
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/utils/bibexport
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibexport.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibexport.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibexport.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Requires:	texlive(bibexport.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A Bourne shell script that uses BibTeX to extract bibliography entries
that are \cite'd in a document. It can also expand a BibTeX file,
expanding the abbreviations (other than the built-in ones like month
names) and following the cross-references.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/texmf-dist
%dir %{_datadir}/texmf-dist/texmf-dist/bibtex
%dir %{_datadir}/texmf-dist/texmf-dist/doc
%dir %{_datadir}/texmf-dist/texmf-dist/scripts
%dir %{_datadir}/texmf-dist/texmf-dist/source
%dir %{_datadir}/texmf-dist/texmf-dist/bibtex/bst
%dir %{_datadir}/texmf-dist/texmf-dist/doc/bibtex
%dir %{_datadir}/texmf-dist/texmf-dist/scripts/bibexport
%dir %{_datadir}/texmf-dist/texmf-dist/source/bibtex
%dir %{_datadir}/texmf-dist/texmf-dist/bibtex/bst/bibexport
%dir %{_datadir}/texmf-dist/texmf-dist/doc/bibtex/bibexport
%dir %{_datadir}/texmf-dist/texmf-dist/source/bibtex/bibexport
%{_datadir}/texmf-dist/texmf-dist/bibtex/bst/bibexport/expcites.bst
%{_datadir}/texmf-dist/texmf-dist/bibtex/bst/bibexport/expkeys.bst
%{_datadir}/texmf-dist/texmf-dist/bibtex/bst/bibexport/export.bst
%doc %{_datadir}/texmf-dist/texmf-dist/doc/bibtex/bibexport/README
%doc %{_datadir}/texmf-dist/texmf-dist/doc/bibtex/bibexport/bibexport.pdf
%{_datadir}/texmf-dist/texmf-dist/scripts/bibexport/bibexport.sh
%doc %{_datadir}/texmf-dist/texmf-dist/source/bibtex/bibexport/bibexport.dtx
%doc %{_datadir}/texmf-dist/texmf-dist/source/bibtex/bibexport/bibexport.ins
