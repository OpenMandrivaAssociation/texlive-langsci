%global tl_name langsci
%global tl_revision 73027

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Typeset books for publication with Language Science Press
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/langsci
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/langsci.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/langsci.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows you to typeset monographs and edited volumes for
publication with Language Science Press (https://www.langsci-press.org).
It includes all necessary files for title pages, frontmatter, main
content, list of references and indexes. Dust jackets for BoD and
Createspace (print-on-demand service providers) can also be produced.

