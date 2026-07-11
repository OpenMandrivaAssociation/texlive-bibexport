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
BuildSystem:	texlive
Requires:	texlive(bibexport.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A Bourne shell script that uses BibTeX to extract bibliography entries
that are \cite'd in a document. It can also expand a BibTeX file,
expanding the abbreviations (other than the built-in ones like month
names) and following the cross-references.

