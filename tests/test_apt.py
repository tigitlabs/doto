import doto.package_manager._apt


def test_apt():
    """
    Test the main
    """
    # Capture the output of the main function and check if it runs without errors
    import io
    from contextlib import redirect_stdout
    f = io.StringIO()
    with redirect_stdout(f):
        doto.package_manager._apt.main()
    output = f.getvalue()
    assert output is not None
    assert isinstance(output, str)
    assert len(output) > 0
    print(output)  # Print the output for visibility in test results
    assert "http" in output or "https" in output  # Check if the output
