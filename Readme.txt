version: 24-11-21

IMPLEMENTATION
~ rename 'help' functions in 'doc'/'documentation'
+ recursive add
+ filtered add (mainly file filter)
+ 'build [<manifest file>]' command
+ 'load <path>' command -> loads a project
  changes should be immediately saved to the current project
! 'load <dir>' automatically searches for the '.htmlbuilder' file
+ 'create <path>' command -> creates a new project
+ error messages

USAGE
! the style of a html file can be specified with '\theme <key>'
  if no style is specified the default style is used
! content files can be added to the manifest file
  with '\include <key>' and whole directories with
  '\includedir <relative path>', specific files can be
  explicitly excluded with '\exclude <key>'
+ snippet files/prefabs that define reused components
! when a style is not found the default style should be used
  and a warning should be given
+ add blocks (translates to '<div/>')
+ add image tag to include images
  these must be connected with the stylesheet
