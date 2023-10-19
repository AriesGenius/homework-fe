#To read a UXF file into a Uxf object use parse() (or parse_options() for finer control),
def read():
let uxt = "uxf 1\n#<File comment>\n{<alpha> 1\n<bravo> 2}\n";
let uxo = uxf::parse(uxt).unwrap(); // -or- pass a filename
assert!(uxt == uxo.to_string())

def relocate:
let uxt = "uxf 1\n=Point x:real y:real\n(Point\n  3.4 -7.4\n  8.0 4.2\n)\n";
let uxo1 = uxf::parse(uxt).unwrap(); // -or- pass a filename
assert!(uxt == uxo1.to_text());
let uxo2 = uxf::parse(&uxo1.to_text()).unwrap(); // round-trip tests:
assert!(uxo1 == uxo2);
assert!(uxo1.to_string() == uxo2.to_string());
assert!(uxo1.to_text() == uxo2.to_text());

#pub use crate::consts::UXF_VERSION;
#pub use crate::consts::VERSION;
#pub use crate::event::ignore_event;
#pub use crate::event::on_event;
#pub use crate::event::Event;
#pub use crate::field::make_field;
#pub use crate::field::make_fields;
#pub use crate::field::Field;
#pub use crate::format::Format;
#pub use crate::list::List;
#pub use crate::map::Map;
#pub use crate::table::NamedRecord;
#pub use crate::table::Table;
#pub use crate::tclass::make_tclass;
#pub use crate::tclass::TClass;
#pub use crate::uxf::parse;
#pub use crate::uxf::parse_options;
#pub use crate::uxf::Compare;
#pub use crate::uxf::ParserOptions;
#pub use crate::uxf::Uxf;
#pub use crate::value::Value;
#pub use crate::value::Visit;
#pub use crate::value::naturalize;


def sorting:
for field in file.classes:
    classes.append(class_)
for table in file.classes:
    classes.append(class_)
for tclass in file.classes:
    classes.append(class_)
for uxf in file(class_):
    classes.append(class_):
for crate in file.classes:
    classes.append(class_)

def compare(ccorrect,user):
    for class_data in class_data:
    if class_data["name"] not in correct_classes:
        wrong_classes.append(class_data)

def compare_answers(answers, correct_answers):
  """Compares the answers with the correct answers and returns a new array of wrong answers."""
  wrong_answers = []

  for answer in answers:
    if len(answer["classes"]) != len(correct_answers["classes"]):
      wrong_answers.append(answer)
      continue

    for class_name, class_attributes in answer["classes"].items():
      if class_name not in correct_answers["classes"]:
        wrong_answers.append(answer)
        break

      if class_attributes != correct_answers["classes"][class_name]:
        wrong_answers.append(answer)
        break

  return wrong_answers

def main():
  answers = [
    {"classes": {"class1": {"attribute1": "value1", "attribute2": "value2"}}, "name": "answer1"},
    {"classes": {"class2": {"attribute3": "value3"}}, "name": "answer2"},
    {"classes": {"class1": {"attribute1": "value1"}}, "name": "answer3"},
  ]

  correct_answers = {
    "classes": {"class1": {"attribute1": "value1", "attribute2": "value2"}}, "name": "correct_answer"}

  wrong_answers = compare_answers(answers, correct_answers)

  print(wrong_answers)

if __name__ == "__main__":
  main()
    
    
