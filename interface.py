def limix.gwas.scan(y, G, F, K, step=1,
                    progress=True, batch_size=1000):
    """Performs genome-wide scan assuming additive model.

    Args:
        y (array_like): unidimensional array of traits.
        F (array_like): nxp array of covariates.
        G (array_like): nxk array of genetic variants.
        K (limix_covariance): covariance.
        step (int): number of variants per test.
        progress (bool): show progress.
        batch_size (int): number of tests per batch. Larger means faster but
                          more memory demanding.

    Returns: dict
        lml-null (float): log of the marginal likelihood for the null hypothesis.
        lml-alt (array_like): log of the marginal likelihoods for the alternative hypotheses.
        alpha-null (array_like): fixed-effect sizes of covariates under the null hypothesis.
        alpha-alt (array_like): fixed-effect sizes of covariates under the alternative hypothesis.
        beta (array_like): fixed-effect sizes of the variant sets.
        p-values (array_like): p-values of tests.
    """
    pass


def limix.gwas.scan_interaction(y, G, F, K, step=1, isize=1, progress=True):
    """Performs genome-wide scan assuming interaction between genetics.

    Args:
        y (array_like): unidimensional array of traits.
        F (array_like): nxp array of covariates.
        G (array_like): nxk array of genetic variants.
        K (limix_covariance): covariance.
        isize (int): number of interacting variants.
        progress (bool): show progress.
        batch_size (int): number of tests per batch. Larger means faster but
                          more memory demanding.

    Returns: dict
        lml-null (float): log of the marginal likelihood for the null hypothesis.
        lml-alt (array_like): log of the marginal likelihoods for the alternative hypotheses.
        alpha-null (array_like): fixed-effect sizes of covariates under the null hypothesis.
        alpha-alt (array_like): fixed-effect sizes of covariates under the alternative hypothesis.
        beta (array_like): fixed-effect sizes of the variant sets.
        p-values (array_like): p-values of tests.
    """
    pass

def limix.gwas.scan_gxe(y, G, F, K, step=1, isize=1, progress=True):
    """Performs genome-wide scan assuming genetic-environment interaction.

    Args:
        y (array_like): unidimensional array of traits.
        F (array_like): nxp array of covariates.
        G (array_like): nxk array of genetic variants.
        K (limix_covariance): covariance.
        isize (int): number of interacting variants.
        progress (bool): show progress.
        batch_size (int): number of tests per batch. Larger means faster but
                          more memory demanding.
    """


def limix.io.utils.fetch_hdf5data(hdf5_data):
    """
    Returns:
        data: dask array.
    """

def limix.io.utils.fetch_hdf5group(hdf5_group, groups=None):
    """
    Args:
        hdf5_group: hdf5 group with datasets of same file
    Returns:
        table: pandas dataframe
    """

def limix.io.read_limix_hdf5(filename, progress=True):
    """
    Args:
        filename (str): name of hdf5 files.
    Returns:
        snp_info: pandas dataframe
        ind_info: pandas dataframe
        data:     geno/pheno
    """

#             sample1 sample2 sample3
# phenoID1     # XXX: yyy      uuuu
# phenoID2
#
#
#             annot1 annot2 annot3
# phenoID1    small
# phenoID2

def limix.io.read_csv(filename, cols=[], memory=True, rows=[]):
    # Danilo solution:
    # df = dask.read_csv(urlpath[, blocksize, collection, ...])
    # df is a dask DataFrame.
    # Example of usage
    # csv = read_csv(pheno_file) # not in memory 60,000 x 1,000
    pass

def limix.io.read_plink(filename, progress=True):
    """
    Args:
        filename (str): prefix to plink files.
    Returns:
        bim: pandas table
        fam: pandas table
        bed: dask
    """
    pass

def limix.io.read_dosage(filename, binary=True, progress=True):
    """
    Returns:
        snp_info: pandas dataframe
        ind_info: pandas dataframe
        geno:     dask
    """
    pass

def limix.plot.manhattan():
    pass

def limix.plot.qqplot():
    pass
