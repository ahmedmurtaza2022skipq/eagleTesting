import aws_cdk as core
import aws_cdk.assertions as assertions

from training_spint1.training_spint1_stack import TrainingSpint1Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in training_spint1/training_spint1_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = TrainingSpint1Stack(app, "training-spint1")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
