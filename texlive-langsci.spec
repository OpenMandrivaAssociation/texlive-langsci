Name:		texlive-langsci
Version:	62061
Release:	1
Summary:	Typeset books for publication with Language Science Press
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/langsci
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/langsci.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/langsci.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows you to typeset monographs and edited
volumes for publication with Language Science Press
(http://www.langsci-press.org). It includes all necessary files
for title pages, frontmatter, main content, list of references
and indexes. Dust jackets for BoD and Createspace
(print-on-demand service providers) can also be produced.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/xelatex/langsci
%doc %{_texmfdistdir}/doc/xelatex/langsci

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
