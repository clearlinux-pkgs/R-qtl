#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-qtl
Version  : 1.60
Release  : 45
URL      : https://cran.r-project.org/src/contrib/qtl_1.60.tar.gz
Source0  : https://cran.r-project.org/src/contrib/qtl_1.60.tar.gz
Summary  : Tools for Analyzing QTL Experiments
Group    : Development/Tools
License  : GPL-3.0
Requires: R-qtl-lib = %{version}-%{release}
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
(called quantitative trait loci, QTLs) contributing to variation in
  quantitative traits.

%package lib
Summary: lib components for the R-qtl package.
Group: Libraries

%description lib
lib components for the R-qtl package.


%prep
%setup -q -n qtl

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1681922469

%install
export SOURCE_DATE_EPOCH=1681922469
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/qtl/BUGS.txt
/usr/lib64/R/library/qtl/CITATION
/usr/lib64/R/library/qtl/DESCRIPTION
/usr/lib64/R/library/qtl/INDEX
/usr/lib64/R/library/qtl/INSTALL_ME.txt
/usr/lib64/R/library/qtl/MQM-TODO.txt
/usr/lib64/R/library/qtl/Meta/Rd.rds
/usr/lib64/R/library/qtl/Meta/data.rds
/usr/lib64/R/library/qtl/Meta/features.rds
/usr/lib64/R/library/qtl/Meta/hsearch.rds
/usr/lib64/R/library/qtl/Meta/links.rds
/usr/lib64/R/library/qtl/Meta/nsInfo.rds
/usr/lib64/R/library/qtl/Meta/package.rds
/usr/lib64/R/library/qtl/Meta/vignette.rds
/usr/lib64/R/library/qtl/NAMESPACE
/usr/lib64/R/library/qtl/NEWS.md
/usr/lib64/R/library/qtl/R/qtl
/usr/lib64/R/library/qtl/R/qtl.rdb
/usr/lib64/R/library/qtl/R/qtl.rdx
/usr/lib64/R/library/qtl/contrib/bin/CMakeLists.txt
/usr/lib64/R/library/qtl/contrib/bin/FindRLibs.cmake
/usr/lib64/R/library/qtl/contrib/bin/README
/usr/lib64/R/library/qtl/contrib/bin/mqmdebugout.cpp
/usr/lib64/R/library/qtl/contrib/bin/mqmmain.cpp
/usr/lib64/R/library/qtl/contrib/bin/regressiontests.bat
/usr/lib64/R/library/qtl/contrib/bin/rtest/regression/mqm_listeria1.rtest
/usr/lib64/R/library/qtl/contrib/bin/rtest/regression/scanone_mr.rtest
/usr/lib64/R/library/qtl/contrib/bin/rtest/test_augmentation.R
/usr/lib64/R/library/qtl/contrib/bin/rtest/test_mqm_hyper_prob.R
/usr/lib64/R/library/qtl/contrib/bin/rtest/test_mqm_listeria1.R
/usr/lib64/R/library/qtl/contrib/bin/rtest/test_scanone_mr.R
/usr/lib64/R/library/qtl/contrib/bin/scripts/cleanup.sh
/usr/lib64/R/library/qtl/contrib/bin/scripts/create-diff.sh
/usr/lib64/R/library/qtl/contrib/bin/scripts/profiler.sh
/usr/lib64/R/library/qtl/contrib/bin/scripts/r.sh
/usr/lib64/R/library/qtl/contrib/bin/scripts/regression_tests.sh
/usr/lib64/R/library/qtl/contrib/bin/scripts/regression_tests_windows.bat
/usr/lib64/R/library/qtl/contrib/bin/test/chrid.dat
/usr/lib64/R/library/qtl/contrib/bin/test/chridhyper.txt
/usr/lib64/R/library/qtl/contrib/bin/test/cofactors.txt
/usr/lib64/R/library/qtl/contrib/bin/test/filledgenohyper.txt
/usr/lib64/R/library/qtl/contrib/bin/test/geno.dat
/usr/lib64/R/library/qtl/contrib/bin/test/genohyper.txt
/usr/lib64/R/library/qtl/contrib/bin/test/markerpos.txt
/usr/lib64/R/library/qtl/contrib/bin/test/markerposhyper.txt
/usr/lib64/R/library/qtl/contrib/bin/test/pheno.dat
/usr/lib64/R/library/qtl/contrib/bin/test/phenohyper.txt
/usr/lib64/R/library/qtl/contrib/bin/test/regression/debugout_dnorm.txt
/usr/lib64/R/library/qtl/contrib/bin/test/regression/debugout_pbeta.txt
/usr/lib64/R/library/qtl/contrib/bin/test/regression/t11out-test0.txt
/usr/lib64/R/library/qtl/contrib/bin/test/regression/t11out.txt
/usr/lib64/R/library/qtl/contrib/bin/test/regression/t12out.txt
/usr/lib64/R/library/qtl/contrib/bin/test/regression/t13out.txt
/usr/lib64/R/library/qtl/contrib/bin/test/regression/t21out.txt
/usr/lib64/R/library/qtl/contrib/bin/test/regression/t22out.txt
/usr/lib64/R/library/qtl/contrib/bin/test/regression/t23out.txt
/usr/lib64/R/library/qtl/contrib/bin/test/regression/t24out.txt
/usr/lib64/R/library/qtl/contrib/bin/test/regression/t25out.txt
/usr/lib64/R/library/qtl/contrib/bin/test/regression/t31out.txt
/usr/lib64/R/library/qtl/contrib/bin/test/regression/t32out.txt
/usr/lib64/R/library/qtl/contrib/bin/test/regression/t33out.txt
/usr/lib64/R/library/qtl/contrib/bin/test/regression/t34out.txt
/usr/lib64/R/library/qtl/contrib/bin/test/settings.dat
/usr/lib64/R/library/qtl/contrib/bin/test/settingshyper.txt
/usr/lib64/R/library/qtl/contrib/bin/test/std/genotypes1.txt
/usr/lib64/R/library/qtl/contrib/bin/test/std/genotypes2.txt
/usr/lib64/R/library/qtl/contrib/bin/test/std/genotypes2m.txt
/usr/lib64/R/library/qtl/contrib/bin/test/std/genotypes3.txt
/usr/lib64/R/library/qtl/contrib/bin/test/std/genotypes3m.txt
/usr/lib64/R/library/qtl/contrib/bin/test/std/markers1.txt
/usr/lib64/R/library/qtl/contrib/bin/test/std/markers2.txt
/usr/lib64/R/library/qtl/contrib/bin/test/std/markers3.txt
/usr/lib64/R/library/qtl/contrib/bin/test/std/phenotypes1.txt
/usr/lib64/R/library/qtl/contrib/bin/test/std/phenotypes2.txt
/usr/lib64/R/library/qtl/contrib/bin/test/std/phenotypes3.txt
/usr/lib64/R/library/qtl/contrib/bin/test/std/settings1.txt
/usr/lib64/R/library/qtl/contrib/bin/test/std/settings2.txt
/usr/lib64/R/library/qtl/contrib/bin/test/std/settings3.txt
/usr/lib64/R/library/qtl/contrib/bin/test/t11/cofactors.txt
/usr/lib64/R/library/qtl/contrib/bin/test/t12/cofactors.txt
/usr/lib64/R/library/qtl/contrib/bin/test/t22/cofactors.txt
/usr/lib64/R/library/qtl/contrib/bin/test/t23/cofactors.txt
/usr/lib64/R/library/qtl/contrib/bin/test/t33/cofactors.txt
/usr/lib64/R/library/qtl/contrib/bin/wincompile.bat
/usr/lib64/R/library/qtl/contrib/biolib/CMakeLists.txt
/usr/lib64/R/library/qtl/contrib/biolib/README
/usr/lib64/R/library/qtl/contrib/scripts/check_rqtl.sh
/usr/lib64/R/library/qtl/contrib/scripts/cleanup.sh
/usr/lib64/R/library/qtl/contrib/scripts/install_rqtl.sh
/usr/lib64/R/library/qtl/contrib/scripts/repl_inputs.rb
/usr/lib64/R/library/qtl/contrib/scripts/run_all_tests.sh
/usr/lib64/R/library/qtl/contrib/scripts/update_header.rb
/usr/lib64/R/library/qtl/data/badorder.RData
/usr/lib64/R/library/qtl/data/bristle3.RData
/usr/lib64/R/library/qtl/data/bristleX.RData
/usr/lib64/R/library/qtl/data/fake.4way.RData
/usr/lib64/R/library/qtl/data/fake.bc.RData
/usr/lib64/R/library/qtl/data/fake.f2.RData
/usr/lib64/R/library/qtl/data/hyper.RData
/usr/lib64/R/library/qtl/data/listeria.RData
/usr/lib64/R/library/qtl/data/locations.RData
/usr/lib64/R/library/qtl/data/map10.RData
/usr/lib64/R/library/qtl/data/mapthis.RData
/usr/lib64/R/library/qtl/data/multitrait.RData
/usr/lib64/R/library/qtl/doc/Sources/MQM/MQM-tour.R
/usr/lib64/R/library/qtl/doc/Sources/MQM/MQM-tour.Rnw
/usr/lib64/R/library/qtl/doc/Sources/MQM/MQM-tour.tex
/usr/lib64/R/library/qtl/doc/Sources/MQM/SweaveIt.R
/usr/lib64/R/library/qtl/doc/Sources/MQM/SweaveIt.Rout
/usr/lib64/R/library/qtl/doc/Sources/MQM/mqm/advantages_Rd.txt
/usr/lib64/R/library/qtl/doc/Sources/MQM/mqm/advantages_latex.txt
/usr/lib64/R/library/qtl/doc/Sources/MQM/mqm/description.txt
/usr/lib64/R/library/qtl/doc/Sources/MQM/mqm/limitations.txt
/usr/lib64/R/library/qtl/doc/Sources/MQM/mqm/parallelisation_references.txt
/usr/lib64/R/library/qtl/doc/Sources/MQM/mqm/significance_references.txt
/usr/lib64/R/library/qtl/doc/Sources/MQM/mqm/standard_example.txt
/usr/lib64/R/library/qtl/doc/Sources/MQM/mqm/standard_references.txt
/usr/lib64/R/library/qtl/doc/Sources/MQM/mqm/standard_seealso.txt
/usr/lib64/R/library/qtl/doc/Sources/MQM/sweaveit.bat
/usr/lib64/R/library/qtl/doc/Sources/MQM/sweaveit.sh
/usr/lib64/R/library/qtl/doc/Sources/geneticmaps.Rnw
/usr/lib64/R/library/qtl/doc/Sources/new_multiqtl.Rnw
/usr/lib64/R/library/qtl/doc/Sources/new_summary_scanone.Rnw
/usr/lib64/R/library/qtl/doc/Sources/new_summary_scantwo.Rnw
/usr/lib64/R/library/qtl/doc/Sources/rqtltour.tex
/usr/lib64/R/library/qtl/doc/Sources/rqtltour2.tex
/usr/lib64/R/library/qtl/doc/bcsft.R
/usr/lib64/R/library/qtl/doc/bcsft.Rnw
/usr/lib64/R/library/qtl/doc/bcsft.pdf
/usr/lib64/R/library/qtl/doc/geneticmaps.R
/usr/lib64/R/library/qtl/doc/geneticmaps.pdf
/usr/lib64/R/library/qtl/doc/index.html
/usr/lib64/R/library/qtl/doc/new_multiqtl.R
/usr/lib64/R/library/qtl/doc/new_multiqtl.pdf
/usr/lib64/R/library/qtl/doc/new_summary_scanone.R
/usr/lib64/R/library/qtl/doc/new_summary_scanone.pdf
/usr/lib64/R/library/qtl/doc/new_summary_scantwo.R
/usr/lib64/R/library/qtl/doc/new_summary_scantwo.pdf
/usr/lib64/R/library/qtl/doc/rqtltour.R
/usr/lib64/R/library/qtl/doc/rqtltour.pdf
/usr/lib64/R/library/qtl/doc/rqtltour2.R
/usr/lib64/R/library/qtl/doc/rqtltour2.pdf
/usr/lib64/R/library/qtl/help/AnIndex
/usr/lib64/R/library/qtl/help/aliases.rds
/usr/lib64/R/library/qtl/help/paths.rds
/usr/lib64/R/library/qtl/help/qtl.rdb
/usr/lib64/R/library/qtl/help/qtl.rdx
/usr/lib64/R/library/qtl/html/00Index.html
/usr/lib64/R/library/qtl/html/R.css
/usr/lib64/R/library/qtl/sampledata/README.txt
/usr/lib64/R/library/qtl/sampledata/gen.txt
/usr/lib64/R/library/qtl/sampledata/listeria.csv
/usr/lib64/R/library/qtl/sampledata/listeria.qtx
/usr/lib64/R/library/qtl/sampledata/listeria_gen.csv
/usr/lib64/R/library/qtl/sampledata/listeria_gen_rot.csv
/usr/lib64/R/library/qtl/sampledata/listeria_map.txt
/usr/lib64/R/library/qtl/sampledata/listeria_maps.txt
/usr/lib64/R/library/qtl/sampledata/listeria_phe.csv
/usr/lib64/R/library/qtl/sampledata/listeria_phe_rot.csv
/usr/lib64/R/library/qtl/sampledata/listeria_qc_cro.txt
/usr/lib64/R/library/qtl/sampledata/listeria_qc_map.txt
/usr/lib64/R/library/qtl/sampledata/listeria_raw.txt
/usr/lib64/R/library/qtl/sampledata/listeria_rot.csv
/usr/lib64/R/library/qtl/sampledata/map.txt
/usr/lib64/R/library/qtl/sampledata/phe.txt
/usr/lib64/R/library/qtl/tests/gen.txt
/usr/lib64/R/library/qtl/tests/listeria.csv
/usr/lib64/R/library/qtl/tests/listeria.map
/usr/lib64/R/library/qtl/tests/listeria.raw
/usr/lib64/R/library/qtl/tests/listeria2.csv
/usr/lib64/R/library/qtl/tests/listeria2.map
/usr/lib64/R/library/qtl/tests/map.txt
/usr/lib64/R/library/qtl/tests/phe.txt
/usr/lib64/R/library/qtl/tests/test_io.R
/usr/lib64/R/library/qtl/tests/test_io.Rout.save
/usr/lib64/R/library/qtl/tests/test_mapqtl_io.R
/usr/lib64/R/library/qtl/tests/test_mapqtl_io.Rout.save
/usr/lib64/R/library/qtl/tests/test_qtl.R
/usr/lib64/R/library/qtl/tests/test_scanonevar.R
/usr/lib64/R/library/qtl/tests/test_scanonevar.Rout.save
/usr/lib64/R/library/qtl/tests/test_tidyIO.R
/usr/lib64/R/library/qtl/tests/test_tidyIO.Rout.save
/usr/lib64/R/library/qtl/tests/testaugmentation.R
/usr/lib64/R/library/qtl/tests/testthat.R
/usr/lib64/R/library/qtl/tests/testthat/test-fliporder.R
/usr/lib64/R/library/qtl/tests/testthat/test-scantwoperm.R
/usr/lib64/R/library/qtl/tests/testthat/test-stepwiseqtl.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/qtl/libs/qtl.so
/usr/lib64/R/library/qtl/libs/qtl.so.avx2
/usr/lib64/R/library/qtl/libs/qtl.so.avx512
