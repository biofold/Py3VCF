"""Smoke tests to verify the vcfaz Python 3 port imports correctly."""

import sys
import os

# Ensure the src/ layout is on the path when running without install
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


def test_import_vcfaz():
    """Test that the vcfaz package can be imported."""
    import vcfaz
    assert vcfaz.__file__ is not None


def test_import_reader():
    """Test that Reader can be imported from vcfaz.parser."""
    from vcfaz.parser import Reader
    assert Reader is not None


def test_import_writer():
    """Test that Writer can be imported from vcfaz.parser."""
    from vcfaz.parser import Writer
    assert Writer is not None


def test_import_vcfreader_alias():
    """Test that VCFReader alias is available."""
    from vcfaz.parser import VCFReader
    from vcfaz.parser import Reader
    assert VCFReader is Reader


def test_import_vcfwriter_alias():
    """Test that VCFWriter alias is available."""
    from vcfaz.parser import VCFWriter
    from vcfaz.parser import Writer
    assert VCFWriter is Writer


def test_import_filter():
    """Test that Filter base class can be imported from vcfaz."""
    import vcfaz
    assert vcfaz.Filter is not None


def test_import_reserved_constants():
    """Test that RESERVED_INFO and RESERVED_FORMAT are available."""
    import vcfaz
    assert isinstance(vcfaz.RESERVED_INFO, dict)
    assert isinstance(vcfaz.RESERVED_FORMAT, dict)
    assert 'DP' in vcfaz.RESERVED_INFO
    assert 'GT' in vcfaz.RESERVED_FORMAT


def test_reader_from_stream():
    """Test that Reader can parse a minimal VCF from a StringIO stream."""
    import io
    from vcfaz.parser import Reader

    vcf_content = (
        "##fileformat=VCFv4.1\n"
        "#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\n"
        "chr1\t100\t.\tA\tG\t50\tPASS\t.\n"
    )
    stream = io.StringIO(vcf_content)
    reader = Reader(fsock=stream)
    records = list(reader)
    assert len(records) == 1
    record = records[0]
    assert record.CHROM == 'chr1'
    assert record.POS == 100
    assert record.REF == 'A'
    assert str(record.ALT[0]) == 'G'
