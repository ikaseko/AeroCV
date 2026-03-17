#let metadata = (
  personal: (
    name: "John",
    email: "john@email.com"
  )
)

#let metadata_mutated = metadata
// Is dictionary mutable? No, Typst variables can't be mutated like metadata.personal.name = "X".
// You have to do metadata.personal.insert("name", "X") if it's a variable, but let's test assignment.
#(metadata_mutated.personal.name = "Alex")

Name is: #(metadata_mutated.personal.name)
