#Compiled By SanzzXD
# Open Sourxe Klo Rame
import marshal,zlib,base64
exec(zlib.decompress(base64.b64decode("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")))
