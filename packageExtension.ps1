#! /usr/bin/pwsh

<#
    .SYNOPSIS
        Script to package and sign the wingwalker Inkscape extension

    .DESCRIPTION
        Simple script to build and sign Inkscape extension.


    .OUTPUTS
        STDOUT, zip file, and signature

    .EXAMPLE
        ./packageExtension.ps1 -sig david.c.days@gmail.com -version 0.1.1

    .NOTES
        All files to be included are listed in this script.  Modifying the script should cover any changes

#>

param(
    <#
        .PARAMETER sig
            The PGP key to use for signing the created zip
    #>
    $sig = "my.name@gmail.com"
)

# Create the distribution directory
$dist = "./dist"
New-Item -ItemType Directory -Force -Path ${dist}

$pkgId = "${dist}/wingwalker"

# Add the extension files
$inxFiles = Get-ChildItem -Path './*.inx'

Compress-Archive -Path ${inxFiles} -DestinationPath "${pkgId}.zip"

$pythonFiles = Get-ChildItem -Path './*.py'

Compress-Archive -Path ${pythonFiles} -Update -DestinationPath "${pkgId}.zip"

# Sign the zip file
& gpg --output "${pkgId}.sig" --detach-sig "${pkgId}.zip"