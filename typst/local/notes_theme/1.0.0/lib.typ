#let theme(body) = {[

#let color_primary = rgb("#c11515")
#let color_secondary = rgb("#51747b")

#set title()
#set heading(numbering: "1.1 -")
#show title: it => {
  set align(center)
  set text(fill: color_secondary)
  it
}
#set par(justify: true)
#show strong: set text(fill: color_primary)

#body
]}

#let styled_block(title, content, comment, stroke_color, fill_color, title_color) = {
  block(
    width: 100%,
    inset: 10pt,
    radius: 5pt,
    stroke: 2pt + stroke_color,
    fill: fill_color,
    [
      #text(size: 1.1em, weight: "bold", fill: title_color, [
        #comment #title
      ]) \
      #content
    ]
  )
}

#let styled_semiblock(title, content, comment, fill_color, title_color) = {
  block(
    width: 100%,
    inset: 10pt,
    fill: fill_color,
    [
      #text(size: 1.1em, weight: "bold", fill: title_color, [
        #comment #title
      ]) \
      #content
    ]
  )
}

#let theorem(title, content) = styled_block(title, content, "Theorem:",
rgb("#61b6cc"), rgb("#ecf6f9"), rgb("#32859a"))
#let property(title, content) = styled_block(title, content, "Property:",
rgb("#a661cc"), rgb("#f4ecf9"), rgb("#76329a"))
#let example(title, content) = styled_block(title, content, "Example:",
rgb("#60cc7a"), rgb("#d9f2df"), rgb("#35974e"))
#let definition(title, content) = styled_semiblock(title, content,
"Definition:", rgb("#d9f2df"), rgb("#35974e"))
