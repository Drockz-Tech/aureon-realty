import vtracer
import sys

try:
    vtracer.convert_image_to_svg_py(
        "logo_transparent.png",
        "logo_traced.svg",
        colormode="color",
        hierarchical="stacked",
        mode="spline",
        filter_speckle=4,
        color_precision=6,
        layer_difference=16,
        corner_threshold=60,
        length_threshold=4.0,
        max_iterations=10,
        splice_threshold=45,
        path_precision=3
    )
    print("Conversion successful: logo_traced.svg")
except Exception as e:
    # Fallback to defaults if specific args fail
    print("Trying with default arguments...")
    vtracer.convert_image_to_svg_py("logo_transparent.png", "logo_traced.svg")
    print("Conversion successful: logo_traced.svg")
