from . import utils
from .globals import table

def get_papers(username):
  if not username:
    return utils.build_response(401, message="All fields required")
  
  res = table.get_item(
    Key={"username": username},
    ProjectionExpression="#papers",
    ExpressionAttributeNames={
      "#papers": "papers"
    }
  )

  if not utils.check_200(res):
    return utils.build_response(402, message="Database interaction failed (get_papers)")

  return utils.build_response(200, papers=list(res["Item"]["papers"]))

def add_paper(link, username):
  # TODO: BATCH WRITE/DELETE
  link = link.strip()
  if not (link and username):
    return utils.build_response(401, message="All fields required.")
  
  res = table.update_item(
    Key={"username":username},
    UpdateExpression="ADD #papers :paper",
    ExpressionAttributeNames={"#papers": "papers"},
    ExpressionAttributeValues={":paper": {link}}
  )
  
  if not utils.check_200(res):
    return utils.build_response(402, message="Database interaction failed (add_paper)")
  
  return utils.build_response(200, message="Successfully added paper.")


  
def remove_paper(link, username):
  link = link.strip()
  if not (link and username):
    return utils.build_response(401, message="All fields required.")
  
  res = table.update_item(
    Key={"username":username},
    UpdateExpression="DELETE #papers :paper",
    ExpressionAttributeNames={"#papers": "papers"},
    ExpressionAttributeValues={":paper": {link}}
  )

  if not utils.check_200(res):
    return utils.build_response(402, message="Database interaction failed (add_paper)")
  
  return utils.build_response(200, message="Successfully deleted paper.")
        